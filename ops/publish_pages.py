"""Track Pages verification and IndexNow submissions in the dedicated publish clone."""
import datetime as dt
import json
import os
import re
import shutil
import subprocess
import sys
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path

SITE = "https://inkisle.ipe.rest"
PENDING = Path(".git/publish-pages.pending")
POST_PATH = re.compile(r"((?:[A-Za-z0-9-]+/)?journal/[a-z0-9-]+/)index\.html")
INDEXNOW_4XX = re.compile(r"^IndexNow inkisle\.ipe\.rest: HTTP (4[0-9]{2}) \([0-9]+ URLs\)$", re.M)
MAX_AGE = dt.timedelta(days=3).total_seconds()
MAX_CLOCK_SKEW = 5 * 60  # seconds
BACKUP_LIMIT = 5
BACKUP_SUFFIX = re.compile(r"\.corrupt-[0-9]{8}-[0-9]{6}-[0-9]{6}")
KST = dt.timezone(dt.timedelta(hours=9))


@dataclass
class PendingURL:
    recorded_at: int
    pages_live: bool = False
    last_submit_day: str = ""


class PendingShapeError(ValueError):
    pass


def log(message):
    print(f"[{dt.datetime.now(KST):%Y-%m-%d %H:%M:%S} KST] publish_daily: {message}", flush=True)


def pending_entry(fields):
    try:
        entry = PendingURL(**fields)
        if type(entry.recorded_at) is not int or entry.recorded_at < 0:
            return None
        if type(entry.pages_live) is not bool:
            return None
        day = entry.last_submit_day
        if day != "" and dt.date.fromisoformat(day).isoformat() != day:
            return None
    except (TypeError, ValueError):
        return None
    return entry


def recover_pending(lock, original, pending, reason):
    timestamp = dt.datetime.now(KST)
    backup = PENDING.with_name(f"{PENDING.name}.corrupt-{timestamp:%Y%m%d-%H%M%S-%f}")
    while backup.exists() or backup.is_symlink():
        timestamp += dt.timedelta(microseconds=1)
        backup = PENDING.with_name(f"{PENDING.name}.corrupt-{timestamp:%Y%m%d-%H%M%S-%f}")
    if original is None:
        try:
            PENDING.rename(backup)
        except OSError as error:
            log(f"WARN — could not move Pages state directory {PENDING} to {backup}: {error}; skipping Pages follow-up")
            return None
    else:
        backup.write_bytes(original)
    log(f"WARN — corrupt Pages state ({reason}); backed up as {backup}")
    if original is not None:
        save_pending(lock, pending)

    # Keep this recovery even if the clock moved back since an earlier backup.
    try:
        earlier = sorted((path for path in PENDING.parent.iterdir()
                          if path != backup and path.name.startswith(PENDING.name)
                          and BACKUP_SUFFIX.fullmatch(path.name[len(PENDING.name):])), reverse=True)
    except OSError as error:
        log(f"WARN — could not list old Pages state backups in {PENDING.parent}: {error}")
        return pending
    for path in earlier[BACKUP_LIMIT - 1:]:
        try:
            if not path.is_symlink() and path.is_dir():
                shutil.rmtree(path)
            else:
                path.unlink(missing_ok=True)
        except OSError as error:
            log(f"WARN — could not remove old Pages state backup {path}: {error}")
    return pending


def parse_pending(content):
    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        if content.lstrip().startswith("{"):
            raise
        # The URL-only format used the file's mtime as the last known update.
        recorded_at = int(PENDING.stat().st_mtime)
        return ((url, pending_entry({"recorded_at": recorded_at})) for url in content.splitlines() if url)
    if not isinstance(data, dict):
        raise PendingShapeError("expected a JSON object")
    return ((url, pending_entry(fields)) for url, fields in data.items())


def load_pending(lock):
    """Return the pending URLs, or None if the state directory could not be moved."""
    try:
        original = PENDING.read_bytes()
    except FileNotFoundError:
        return {}
    except IsADirectoryError:
        return recover_pending(lock, None, {}, "state path is a directory")
    if not original:
        log("WARN — Pages state file is empty; starting with no pending URLs")
        PENDING.unlink(missing_ok=True)
        return {}
    try:
        entries = parse_pending(original.decode("utf-8"))
    except PendingShapeError as error:
        return recover_pending(lock, original, {}, str(error))
    except (ValueError, RecursionError):
        return recover_pending(lock, original, {}, "malformed JSON or UTF-8")

    pending = {}
    invalid = 0
    future = 0
    latest = int(dt.datetime.now(KST).timestamp()) + MAX_CLOCK_SKEW
    for url, entry in entries:
        path = url[len(SITE) + 1:] + "index.html"
        if entry is None or not url.startswith(f"{SITE}/") or not POST_PATH.fullmatch(path):
            invalid += 1
        elif entry.recorded_at > latest:
            future += 1
        else:
            pending[url] = entry
    reasons = []
    if invalid:
        reasons.append(f"skipped {invalid} invalid URL entry(s)")
    if future:
        reasons.append(f"expired {future} URL entry(s) with future recorded_at")
    if reasons:
        return recover_pending(lock, original, pending, "; ".join(reasons))
    return pending


def save_pending(lock, pending):
    if not pending:
        PENDING.unlink(missing_ok=True)
        return
    tmp = lock / "pages.pending"
    tmp.write_text(json.dumps({url: asdict(entry) for url, entry in pending.items()}, sort_keys=True, indent=2) + "\n",
                   encoding="utf-8")
    tmp.replace(PENDING)


def remember(lock, paths):
    matches = (POST_PATH.fullmatch(path) for path in paths)
    urls = [f"{SITE}/{match[1]}" for match in matches if match]
    if not urls:
        return
    pending = load_pending(lock)
    if pending is None:
        return
    recorded_at = int(dt.datetime.now(KST).timestamp())
    for url in urls:
        pending.setdefault(url, PendingURL(recorded_at))
    save_pending(lock, pending)
    # This list is only for this run, which reaches verification after the push succeeds.
    with (lock / "pages.new").open("a", encoding="utf-8") as fresh:
        fresh.write("\n".join(urls) + "\n")


def pages_are_live(urls, cache_key):
    for url in urls:
        try:
            response = subprocess.run(
                ["curl", "--disable", "--silent", "--max-time", "10", "--output", "/dev/null",
                 "--write-out", "%{http_code}", "--header", "Cache-Control: no-cache", f"{url}?v={cache_key}"],
                capture_output=True, text=True,
            )
        except OSError:
            log(f"Pages pending (curl unavailable): {url}")
            return False
        if response.returncode or response.stdout != "200":
            log(f"Pages pending (HTTP {response.stdout or 'unknown'}): {url}")
            return False
    return True


def verify_fresh_pages(groups, cache_key):
    live = []
    for attempt in range(3):
        if attempt:
            log(f"Pages retry {attempt}/2 — dispatching a fresh workflow on main")
            try:
                dispatched = subprocess.run(["gh", "workflow", "run", "Deploy to GitHub Pages", "--ref", "main"]).returncode == 0
            except OSError:
                dispatched = False
            if not dispatched:
                log(f"WARN — Pages retry {attempt}/2 dispatch failed (check gh and Actions permissions)")
        subprocess.run(["sleep", "120"], check=True)
        for probe in range(1, 8):
            for slug, urls in list(groups.items()):
                if pages_are_live(urls, f"{cache_key}-{attempt}-{probe}"):
                    live.extend(groups.pop(slug))
            if not groups:
                return live
            if probe < 7:
                subprocess.run(["sleep", "30"], check=True)
    return live


def submit_ready(lock, pending, today):
    urls = sorted(url for url, entry in pending.items() if entry.pages_live and entry.last_submit_day < today)
    if not urls:
        return
    # Record before sending so an interrupted run cannot repeat the request that day.
    for url in urls:
        pending[url].last_submit_day = today
    save_pending(lock, pending)
    result = subprocess.run([sys.executable, "scripts/indexnow.py", *urls, f"{SITE}/", f"{SITE}/journal/"],
                            capture_output=True, text=True)
    sys.stdout.write(result.stdout)
    sys.stderr.write(result.stderr)
    rejected = INDEXNOW_4XX.search(result.stdout)
    if result.returncode == 0:
        log(f"IndexNow submitted — {len(urls)} journal URL(s)")
    elif rejected and rejected[1] != "429":
        log(f"WARN — IndexNow HTTP {rejected[1]}; dropping {len(urls)} URL(s) from submission retry")
    else:
        log(f"WARN — INDEXNOW_PENDING; {len(urls)} URL(s) eligible for submission on a later KST day before expiry")
        return
    for url in urls:
        del pending[url]
    save_pending(lock, pending)


def verify(lock):
    pending = load_pending(lock)
    if not pending:
        return 0
    now = dt.datetime.now(KST)
    for url, entry in list(pending.items()):
        path = url[len(SITE) + 1:] + "index.html"
        if not Path(path).is_file():
            del pending[url]
        elif now.timestamp() - entry.recorded_at >= MAX_AGE:
            log(f"WARN — pending URL expired after 72 hours; dropping from follow-up: {url}")
            del pending[url]

    fresh_path = lock / "pages.new"
    fresh = set(fresh_path.read_text(encoding="utf-8").splitlines()) if fresh_path.is_file() else set()
    fresh_groups, earlier_groups = defaultdict(list), defaultdict(list)
    for url, entry in sorted(pending.items()):
        if not entry.pages_live:
            groups = fresh_groups if url in fresh else earlier_groups
            groups[url.split("/")[-2]].append(url)

    cache_key = f"{int(now.timestamp())}-{os.getpid()}"
    live = verify_fresh_pages(fresh_groups, cache_key) if fresh_groups else []
    for urls in earlier_groups.values():
        if pages_are_live(urls, f"{cache_key}-0-1"):
            live.extend(urls)
    for url in live:
        pending[url].pages_live = True
    if live:
        log(f"Pages live — {len(live)} URL(s) returned HTTP 200")
    save_pending(lock, pending)
    submit_ready(lock, pending, dt.datetime.now(KST).date().isoformat())
    if any(not entry.pages_live for entry in pending.values()):
        log("FAIL — PAGES_NOT_LIVE; unverified URLs kept for the next eligible check")
        return 1
    log("Pages follow-up complete")
    return 0


if __name__ == "__main__":
    action, lock_path = sys.argv[1:]
    if action not in {"remember", "verify"}:
        sys.exit(f"unknown Pages action: {action}")
    try:
        if action == "remember":
            remember(Path(lock_path), sys.stdin.read().splitlines())
        else:
            sys.exit(verify(Path(lock_path)))
    except OSError as error:
        if action == "remember":
            sys.exit(f"Pages state error: {error}")
        # State I/O errors stop follow-up for this run. The explicit PAGES_NOT_LIVE exit still propagates.
        log(f"WARN — could not finish Pages/IndexNow follow-up: {error}")
