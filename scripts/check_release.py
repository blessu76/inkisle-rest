#!/usr/bin/env python3
"""Release-note gate for one app build — stdlib only. Exit 0 = ready, exit 1 = something is missing.

  python3 scripts/check_release.py --build 7          # 1.0.0+7 is in content/releases.json in all 12 languages
  python3 scripts/check_release.py --build 1.0.0+7    # same (the pubspec spelling is accepted)

The app repo's deploy_ios.sh calls this before it uploads a build, so a TestFlight build can no longer go out
without its release note (builds 6 and 7 once did). What it checks for the entry whose `build` is N:
  1. the entry exists in content/releases.json (and its id / status / date look right);
  2. title, intro and notes are filled in for every language in LANGS (en ko ja zh es fr de pt ru ar hi id) —
     build_site.py itself only insists on en + ko and quietly shows English elsewhere;
  3. every language has the same number of notes as English;
  4. the generated pages (releases/index.html and <lang>/releases/index.html) already contain the entry,
     i.e. `python3 scripts/build_site.py` has been run.
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_site as bs  # noqa: E402


def parse_build(raw):
    """'7' or '1.0.0+7' -> '7'; None if it is neither."""
    m = re.match(r"^(?:\d+(?:\.\d+)*\+)?(\d+)$", str(raw).strip())
    return str(int(m.group(1))) if m else None


def check(root, build, pages=True):
    """-> list of problems (empty = the note for [build] is complete)."""
    root = Path(root)
    n = parse_build(build)
    if n is None:
        return ["--build must be a build number such as 7 or 1.0.0+7, got %r" % build]
    f = root / "content" / "releases.json"
    if not f.is_file():
        return ["content/releases.json: missing"]
    entries, errs = bs.load_releases(root)
    errs = list(errs)
    if not entries and errs:
        return errs
    hits = [e for e in entries if str(e.get("build", "")) == n]
    if not hits:
        return errs + ["build %s: no entry in content/releases.json (add one with all %d languages)" % (n, len(bs.LANGS))]
    if len(hits) > 1:
        errs.append("build %s: %d entries in content/releases.json, expected one" % (n, len(hits)))
    e = hits[0]
    if e.get("id") != "%s-%s" % (e.get("version"), n):
        errs.append("build %s: id %r should be %r" % (n, e.get("id"), "%s-%s" % (e.get("version"), n)))
    if e.get("status") == "testflight" and not e.get("date"):
        errs.append("build %s: status testflight needs a date" % n)
    missing = []
    for field in ("title", "intro", "notes"):
        v = e.get(field) if isinstance(e.get(field), dict) else {}
        for lang in bs.LANGS:
            val = v.get(lang)
            if not val or (field == "notes" and not isinstance(val, list)):
                missing.append("%s.%s" % (field, lang))
    if missing:
        errs.append("build %s: missing %s" % (n, ", ".join(missing)))
    notes = e.get("notes") if isinstance(e.get("notes"), dict) else {}
    en_n = len(notes.get("en") or [])
    for lang in bs.LANGS:
        if isinstance(notes.get(lang), list) and notes[lang] and len(notes[lang]) != en_n:
            errs.append("build %s: notes.%s has %d items, en has %d" % (n, lang, len(notes[lang]), en_n))
    if pages:
        for lang in bs.LANGS:
            page = root / bs.path_releases(lang).strip("/") / "index.html"
            if not page.is_file():
                errs.append("build %s: %s missing (run: python3 scripts/build_site.py)" % (n, page.relative_to(root)))
            elif 'id="%s"' % e.get("id") not in page.read_text(encoding="utf-8"):
                errs.append("build %s: %s is stale (run: python3 scripts/build_site.py)" % (n, page.relative_to(root)))
    return errs


def main(argv=None):
    ap = argparse.ArgumentParser(description="Check that the release note for an app build is complete (12 languages).")
    ap.add_argument("--build", required=True, help="build number, e.g. 7 or 1.0.0+7")
    ap.add_argument("--root", default=str(Path(__file__).resolve().parent.parent), help="site repo root (default: this repo)")
    ap.add_argument("--no-pages", action="store_true", help="skip the check of the generated pages")
    a = ap.parse_args(argv)
    errs = check(a.root, a.build, pages=not a.no_pages)
    if errs:
        print("release note NOT ready:")
        for x in errs:
            print("  - " + x)
        return 1
    print("release note for build %s: OK (%d languages)" % (parse_build(a.build), len(bs.LANGS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
