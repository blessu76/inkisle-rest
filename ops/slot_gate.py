#!/usr/bin/env python3
"""Random afternoon publish slot gate (KST). Called every 15 min by launchd (12:00-18:45 ticks); decides whether ops/publish_daily.sh runs now.

State file (INKISLE_SLOT_FILE, default ~/.ipe/queue/inkisle/slot.json):
  {"date": "YYYY-MM-DD", "time": "HH:MM", "prev_date": ..., "prev_time": ..., "published": true|false}
A new day draws a new time in 12:00-17:29 whose hour differs from yesterday's hour (the 17:xx hour only uses minutes 0-29,
so at least two 15-min ticks remain before 18:00 for a retry). HARD CUTOFF: from 18:00 on (hm >= "18:00") nothing is ever published that day. Test hooks: INKISLE_NOW="YYYY-MM-DD HH:MM",
INKISLE_PUBLISH_CMD (default: bash <ops>/publish_daily.sh).
"""
import datetime as dt
import json
import os
import random
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CUTOFF = "18:00"             # hard cutoff: at/after this the gate never publishes (a missed day is skipped, not retried in the evening)
LAST_SLOT_MINUTE_17 = 29     # 17:xx draws only minutes 0-29 so >= 2 ticks (e.g. 17:30, 17:45) fit before the cutoff
DONE_RE = re.compile(r"publish_daily: (pushed \S+|nothing to publish)")


def now_kst():
    inj = os.environ.get("INKISLE_NOW")
    if inj:
        return dt.datetime.strptime(inj, "%Y-%m-%d %H:%M")
    return dt.datetime.now(dt.timezone(dt.timedelta(hours=9))).replace(tzinfo=None)


def draw(prev_time, rng=random):
    prev_hour = int(prev_time.split(":")[0]) if prev_time else None
    hours = [h for h in range(12, 18) if h != prev_hour]
    hour = rng.choice(hours)
    minute = rng.randrange(LAST_SLOT_MINUTE_17 + 1 if hour == 17 else 60)
    return "%02d:%02d" % (hour, minute)


def load(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def save(path, state):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, indent=1) + "\n", encoding="utf-8")
    os.replace(tmp, path)


def log(msg, now):
    print("[%s KST] slot_gate: %s" % (now.strftime("%Y-%m-%d %H:%M:%S"), msg), flush=True)


def main():
    path = Path(os.environ.get("INKISLE_SLOT_FILE") or Path.home() / ".ipe/queue/inkisle/slot.json")
    now = now_kst()
    today, hm = now.strftime("%Y-%m-%d"), now.strftime("%H:%M")
    st = load(path)
    if st.get("date") != today:
        st = {"date": today, "time": draw(st.get("time")), "prev_date": st.get("date"), "prev_time": st.get("time"), "published": False}
        save(path, st)
        log("new slot for %s: %s (previous %s %s)" % (today, st["time"], st["prev_date"], st["prev_time"]), now)
    if st.get("published"):
        return 0
    if hm < st["time"]:
        return 0
    if hm >= CUTOFF:
        log("at/after %s — hard cutoff, not publishing today" % CUTOFF, now)
        return 0
    cmd = os.environ.get("INKISLE_PUBLISH_CMD") or "bash %s/publish_daily.sh" % HERE
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    sys.stdout.write(r.stdout + r.stderr)
    if r.returncode == 0 and DONE_RE.search(r.stdout + r.stderr):
        st["published"] = True
        save(path, st)
        log("published — slot done for %s" % today, now)
    else:
        log("not published (rc=%d) — retry next tick" % r.returncode, now)
    return 0


if __name__ == "__main__":
    sys.exit(main())
