"""ops/publish_daily.sh safety rules, run against a throw-away origin + publish clone (no network, no real check.sh)."""
import datetime as dt
import json
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import helpers
from helpers import REPO
from ops import publish_pages

SCRIPT = REPO / "ops" / "publish_daily.sh"
PAST = "2026-10-01T19:00+09:00"


def git(cwd, *args, check=True):
    return subprocess.run(["git", *args], cwd=cwd, check=check, capture_output=True, text=True,
                          env={**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t", "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t"})


class PublishDaily(unittest.TestCase):
    def setUp(self):
        site = helpers.make_site(posts=(("alpha-post", PAST),), queue=("next-one", "next-two"))
        self.addCleanup(shutil.rmtree, site, True)
        shutil.copytree(REPO / "scripts", site / "scripts", ignore=shutil.ignore_patterns("__pycache__"))
        # The real repo ignores __pycache__; without it, CI's Python (which writes bytecode next to the scripts the
        # publish run imports) leaves an untracked scripts/__pycache__ and the "unexpected paths" guard rolls back.
        shutil.copy(REPO / ".gitignore", site / ".gitignore")
        shutil.copytree(REPO / "vendor", site / "vendor", ignore=shutil.ignore_patterns("__pycache__"))  # build_site imports ipe_web_kit from vendor/
        helpers.build(site)
        self.tmp = Path(tempfile.mkdtemp(prefix="inkisle-pd-"))
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.home = self.tmp / "home"
        self.home.mkdir()
        self.origin = self.tmp / "origin.git"
        git(self.tmp, "init", "-q", "--bare", "-b", "main", str(self.origin))
        self.clone = site
        self.pending = self.clone / ".git" / "publish-pages.pending"
        git(site, "init", "-q", "-b", "main")
        git(site, "add", "-A")
        git(site, "commit", "-q", "-m", "init")
        git(site, "remote", "add", "origin", str(self.origin))
        git(site, "push", "-q", "origin", "main")
        self.check_cmd = "true"

    def run_script(self, check_cmd=None, publish_dir=None, **extra):
        # The fixture clone has no vendor/ipe_web_kit.lock, so the kit check is stubbed out unless a test supplies its own.
        extra = {"INKISLE_KIT_CHECK_CMD": "true", "INKISLE_SKIP_NET": "1", **extra}
        env = helpers.isolated_env(self.home, INKISLE_PUBLISH_DIR=str(publish_dir or self.clone), INKISLE_CHECK_CMD=check_cmd or self.check_cmd,
                                   **extra, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t", GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t")
        return subprocess.run(["bash", str(SCRIPT)], capture_output=True, text=True, env=env)

    def pages_stubs(self, live_after=0, dispatch_error=False):
        """Replace every network and sleep command in the post-push path inside the fixture."""
        bin_dir = self.tmp / "bin"
        bin_dir.mkdir()
        self.pages_trace = self.tmp / "pages.log"
        commands = {
            "curl": '''
for arg do url=$arg; done
printf 'probe %s\n' "$url" >> "$PAGES_TRACE"
dispatched=$(grep -c '^dispatch ' "$PAGES_TRACE")
if [ -n "${PAGES_BLOCKED:-}" ] && [ "${url%%[?]*}" = "$PAGES_BLOCKED" ]; then
  printf 404
  exit 0
fi
case "$url" in
  */ko/*) [ "${PAGES_READY:-0}" = 1 ] || [ "$dispatched" -ge "$LIVE_AFTER" ] ;;
  *) true ;;
esac && printf 200 || printf 404
''',
            "gh": '''
printf 'dispatch [%s][%s][%s][%s][%s]\n' "$@" >> "$PAGES_TRACE"
[ "$GH_PROMPT_DISABLED" = 1 ] && [ "$DISPATCH_ERROR" = 0 ]
''',
            "sleep": '''printf 'sleep %s\n' "$*" >> "$PAGES_TRACE"\n''',
        }
        for name, command in commands.items():
            stub = bin_dir / name
            stub.write_text("#!/bin/sh\n" + command)
            stub.chmod(0o755)
        (self.clone / "scripts/indexnow.py").write_text(
            "import os, sys\nwith open(os.environ['PAGES_TRACE'], 'a') as f:\n"
            "    f.write('indexnow ' + ' '.join(sys.argv[1:]) + '\\n')\n"
            "if status := os.environ.get('INDEXNOW_STATUS'):\n"
            "    print(f'IndexNow inkisle.ipe.rest: HTTP {status} ({len(sys.argv) - 1} URLs)')\n"
            "    sys.exit(int(status not in ('200', '202')))\n"
            "sys.exit(int(os.environ.get('INDEXNOW_ERROR', '0')))\n"
        )
        git(self.clone, "commit", "-qam", "stub IndexNow")
        git(self.clone, "push", "-q", "origin", "main")
        return dict(INKISLE_SKIP_NET="0", PATH=str(bin_dir) + os.pathsep + os.environ["PATH"],
                    PAGES_TRACE=str(self.pages_trace), LIVE_AFTER=str(live_after), DISPATCH_ERROR=str(int(dispatch_error)))

    def test_pages_live_after_push_needs_no_dispatch(self):
        r = self.run_script(**self.pages_stubs())
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        trace = self.pages_trace.read_text().splitlines()
        self.assertEqual(trace[0], "sleep 120")
        self.assertRegex(trace[1], r"^probe https://inkisle\.ipe\.rest/journal/next-one/\?v=\d+-\d+-0-1$")
        cache_query = trace[1].split("?", 1)[1]
        self.assertEqual(trace[2:], [
            f"probe https://inkisle.ipe.rest/ko/journal/next-one/?{cache_query}",
            "indexnow https://inkisle.ipe.rest/journal/next-one/ https://inkisle.ipe.rest/ko/journal/next-one/ "
            "https://inkisle.ipe.rest/ https://inkisle.ipe.rest/journal/",
        ])

    def test_missing_localized_page_dispatches_a_fresh_run_before_indexnow(self):
        r = self.run_script(**self.pages_stubs(live_after=1))
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        trace = self.pages_trace.read_text().splitlines()
        dispatch = "dispatch [workflow][run][Deploy to GitHub Pages][--ref][main]"
        self.assertEqual([line for line in trace if line.startswith("dispatch ")], [dispatch])
        self.assertEqual(trace.count("sleep 30"), 6)
        self.assertEqual(trace[trace.index(dispatch) + 1], "sleep 120")
        probes = [line for line in trace if line.startswith("probe https://inkisle.ipe.rest/ko/")]
        self.assertEqual(len(probes), 8)
        self.assertEqual(len(set(probes)), 8)  # even when fake sleep leaves probes in the same second
        self.assertRegex(probes[-1], r"/next-one/\?v=\d+-\d+-1-1$")
        self.assertTrue(trace[-1].startswith("indexnow "))

    def test_pages_retries_stop_after_two_even_if_dispatch_fails(self):
        r = self.run_script(**self.pages_stubs(live_after=3, dispatch_error=True))
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("PAGES_NOT_LIVE", r.stdout)
        self.assertEqual(r.stdout.count("dispatch failed"), 2)
        trace = self.pages_trace.read_text().splitlines()
        self.assertEqual(sum(line.startswith("dispatch ") for line in trace), 2)
        self.assertEqual(trace.count("sleep 30"), 18)
        self.assertEqual(trace.count("sleep 120"), 3)
        self.assertTrue(all(trace[i + 1] == "sleep 120" for i, line in enumerate(trace) if line.startswith("dispatch ")))
        self.assertFalse(any(line.startswith("indexnow ") for line in trace))
        self.assertEqual(self.head(), self.origin_head())
        self.assertEqual(git(self.clone, "status", "--porcelain").stdout, "")
        self.assertFalse((self.clone / ".git" / "publish.lock").exists())

    def test_recovered_push_also_verifies_pages_when_today_has_a_post(self):
        env = self.pages_stubs(live_after=2)
        hook = self.origin / "hooks" / "pre-receive"
        hook.write_text("#!/bin/sh\nexit 1\n")
        hook.chmod(0o755)
        first = self.run_script(**env)
        self.assertIn("commit kept locally", first.stdout)
        self.assertFalse(self.pages_trace.exists())
        hook.unlink()
        second = self.run_script(**env)
        self.assertEqual(second.returncode, 0, second.stdout + second.stderr)
        self.assertIn("nothing to publish", second.stdout)
        self.assertIn("Pages live", second.stdout)
        trace = self.pages_trace.read_text().splitlines()
        self.assertEqual(sum(line.startswith("dispatch ") for line in trace), 2)
        self.assertEqual(sum(line.startswith("indexnow ") for line in trace), 1)

    def test_truncated_pending_json_is_backed_up_before_pushing_new_post(self):
        env = self.pages_stubs()
        original = b'{"https://inkisle.ipe.rest/journal/alpha-post/":'
        self.pending.write_bytes(original)
        before = self.origin_head()

        result = self.run_script(**env)

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("WARN — corrupt Pages state (malformed JSON or UTF-8)", result.stdout)
        self.assertIn("pushed next-one", result.stdout)
        self.assertIn("IndexNow submitted", result.stdout)
        self.assertNotEqual(before, self.origin_head())
        self.assertEqual(self.head(), self.origin_head())
        self.assertFalse(self.pending.exists())
        self.assertEqual([p.read_bytes() for p in self.pending.parent.glob("publish-pages.pending.corrupt-*")], [original])

    def test_invalid_pending_entries_are_skipped_before_retrying_push(self):
        env = self.pages_stubs()
        hook = self.origin / "hooks" / "pre-receive"
        hook.write_text("#!/bin/sh\nexit 1\n")
        hook.chmod(0o755)
        before = self.origin_head()
        first = self.run_script(**env)
        self.assertIn("commit kept locally", first.stdout)
        hook.unlink()

        now = int(dt.datetime.now(dt.timezone.utc).timestamp())
        old = "https://inkisle.ipe.rest/journal/alpha-post/"
        pending = json.loads(self.pending.read_text())
        pending[old] = {"recorded_at": now}
        pending["https://inkisle.ipe.rest/ko/journal/alpha-post/"] = {"recorded_at": now, "unknown": True}
        pending["https://inkisle.ipe.rest/en/journal/alpha-post/"] = {"recorded_at": "invalid"}
        original = json.dumps(pending).encode("utf-8")
        self.pending.write_bytes(original)

        result = self.run_script(**env, PAGES_BLOCKED=old)

        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)  # old page still pending
        self.assertIn("WARN — corrupt Pages state (skipped 2 invalid URL entry(s))", result.stdout)
        self.assertIn("pushed earlier publication commit(s)", result.stdout)
        self.assertIn("IndexNow submitted", result.stdout)
        self.assertIn("PAGES_NOT_LIVE", result.stdout)
        self.assertNotEqual(before, self.origin_head())
        self.assertEqual(self.head(), self.origin_head())
        self.assertEqual(json.loads(self.pending.read_text()), {
            old: {"recorded_at": now, "pages_live": False, "last_submit_day": ""},
        })
        self.assertEqual([p.read_bytes() for p in self.pending.parent.glob("publish-pages.pending.corrupt-*")], [original])

    def test_next_tick_checks_pending_urls_when_nothing_is_due(self):
        env = self.pages_stubs(live_after=3)
        first = self.run_script(**env)
        self.assertEqual(first.returncode, 1, first.stdout + first.stderr)
        self.assertIn("PAGES_NOT_LIVE", first.stdout)
        published = self.origin_head()
        self.pages_trace.write_text("")

        pending = self.run_script(**env)
        self.assertEqual(pending.returncode, 1, pending.stdout + pending.stderr)
        self.assertIn("nothing to publish", pending.stdout)
        self.assertIn("PAGES_NOT_LIVE", pending.stdout)
        self.assertNotIn("ROLLBACK", pending.stdout)
        self.assertEqual(len(self.pages_trace.read_text().splitlines()), 2)
        self.assertTrue(all(line.startswith("probe ") for line in self.pages_trace.read_text().splitlines()))
        self.pages_trace.write_text("")

        ready = self.run_script(**env, PAGES_READY="1")
        self.assertEqual(ready.returncode, 0, ready.stdout + ready.stderr)
        self.assertIn("Pages follow-up complete", ready.stdout)
        self.assertEqual([line.split()[0] for line in self.pages_trace.read_text().splitlines()], ["probe", "probe", "indexnow"])
        self.assertEqual(self.origin_head(), published)
        self.pages_trace.write_text("")
        self.assertEqual(self.run_script(**env).returncode, 0)
        self.assertEqual(self.pages_trace.read_text(), "")

    def test_empty_queue_retries_indexnow_on_a_later_day_without_rechecking_pages(self):
        env = self.pages_stubs()
        git(self.clone, "rm", "-qr", "content/queue/02-next-two")
        git(self.clone, "commit", "-qm", "one queued post left")
        git(self.clone, "push", "-q", "origin", "main")
        hook = self.origin / "hooks" / "pre-receive"
        hook.write_text("#!/bin/sh\nexit 1\n")
        hook.chmod(0o755)
        first = self.run_script(**env)
        self.assertIn("commit kept locally", first.stdout)
        self.assertFalse(self.pages_trace.exists())
        hook.unlink()

        recovered = self.run_script(**env, INDEXNOW_STATUS="503")
        self.assertEqual(recovered.returncode, 0, recovered.stdout + recovered.stderr)
        self.assertIn("QUEUE_EMPTY", recovered.stdout)
        self.assertIn("INDEXNOW_PENDING", recovered.stdout)
        self.assertIn("Pages follow-up complete", recovered.stdout)
        self.assertEqual([line.split()[0] for line in self.pages_trace.read_text().splitlines()],
                         ["sleep", "probe", "probe", "indexnow"])
        published = self.origin_head()
        self.pages_trace.write_text("")

        for _ in range(2):
            same_day = self.run_script(**env, INDEXNOW_STATUS="503")
            self.assertEqual(same_day.returncode, 0, same_day.stdout + same_day.stderr)
            self.assertIn("Pages follow-up complete", same_day.stdout)
            self.assertEqual(self.pages_trace.read_text(), "")

        pending = json.loads(self.pending.read_text())
        for entry in pending.values():
            last_submit_day = dt.date.fromisoformat(entry["last_submit_day"])
            entry["last_submit_day"] = (last_submit_day - dt.timedelta(days=1)).isoformat()
        self.pending.write_text(json.dumps(pending))
        ready = self.run_script(**env)
        self.assertEqual(ready.returncode, 0, ready.stdout + ready.stderr)
        self.assertIn("QUEUE_EMPTY", ready.stdout)
        self.assertIn("IndexNow submitted", ready.stdout)
        self.assertEqual([line.split()[0] for line in self.pages_trace.read_text().splitlines()], ["indexnow"])
        self.assertFalse(self.pending.exists())
        self.assertEqual(self.origin_head(), published)

    def test_expired_pending_urls_are_dropped_without_a_probe(self):
        env = self.pages_stubs(live_after=3)
        first = self.run_script(**env)
        self.assertIn("PAGES_NOT_LIVE", first.stdout)
        pending = json.loads(self.pending.read_text())
        for entry in pending.values():
            entry["recorded_at"] -= 3 * 24 * 60 * 60
        self.pending.write_text(json.dumps(pending))
        self.pages_trace.write_text("")

        later = self.run_script(**env)
        self.assertEqual(later.returncode, 0, later.stdout + later.stderr)
        self.assertEqual(later.stdout.count("pending URL expired after 72 hours"), 2)
        self.assertFalse(self.pending.exists())
        self.assertEqual(self.pages_trace.read_text(), "")

    def test_old_blocked_post_cannot_block_indexnow_for_a_new_post(self):
        env = self.pages_stubs()
        old_url = "https://inkisle.ipe.rest/ko/journal/alpha-post/"
        self.pending.write_text(old_url + "\n")
        recorded_at = int(self.pending.stat().st_mtime) - 24 * 60 * 60
        os.utime(self.pending, (recorded_at, recorded_at))

        result = self.run_script(**env, PAGES_BLOCKED=old_url)
        self.assertIn("PAGES_NOT_LIVE", result.stdout)
        trace = self.pages_trace.read_text().splitlines()
        self.assertTrue(any(line.startswith(f"probe {old_url}?") for line in trace))
        self.assertFalse(any(line.startswith("dispatch ") for line in trace))
        self.assertEqual([line for line in trace if line.startswith("indexnow ")], [
            "indexnow https://inkisle.ipe.rest/journal/next-one/ https://inkisle.ipe.rest/ko/journal/next-one/ "
            "https://inkisle.ipe.rest/ https://inkisle.ipe.rest/journal/",
        ])
        self.assertEqual(json.loads(self.pending.read_text()), {
            old_url: {"recorded_at": recorded_at, "pages_live": False, "last_submit_day": ""},
        })
        self.assertEqual(self.head(), self.origin_head())

    def test_indexnow_client_error_is_dropped_from_retry(self):
        env = self.pages_stubs()
        result = self.run_script(**env, INDEXNOW_STATUS="403")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("IndexNow HTTP 403; dropping 2 URL(s)", result.stdout)
        self.assertNotIn("INDEXNOW_PENDING", result.stdout)
        self.assertIn("Pages follow-up complete", result.stdout)
        self.assertFalse(self.pending.exists())
        self.pages_trace.write_text("")

        later = self.run_script(**env, INDEXNOW_STATUS="403")
        self.assertEqual(later.returncode, 0, later.stdout + later.stderr)
        self.assertEqual(self.pages_trace.read_text(), "")

    def test_removed_url_does_not_block_the_remaining_pending_urls(self):
        env = self.pages_stubs(live_after=3)
        r = self.run_script(**env)
        self.assertIn("PAGES_NOT_LIVE", r.stdout)
        git(self.clone, "rm", "-q", "ko/journal/next-one/index.html")
        git(self.clone, "commit", "-qm", "remove localized page")
        git(self.clone, "push", "-q", "origin", "main")
        self.pages_trace.write_text("")

        r = self.run_script(**env)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        trace = self.pages_trace.read_text().splitlines()
        self.assertEqual([line.split()[0] for line in trace], ["probe", "indexnow"])
        self.assertFalse(any("/ko/" in line for line in trace))

    def test_default_publish_dir_comes_from_home_and_tests_never_see_the_real_one(self):
        # Regression: the tests must not be able to reach the real publish clone / log. With HOME isolated and no INKISLE_PUBLISH_DIR the script
        # resolves ~/Developer/inkisle-rest inside the temp home, finds no clone and skips — and writes nothing there.
        env = helpers.isolated_env(self.home, INKISLE_SKIP_NET="1")
        self.assertNotIn("INKISLE_PUBLISH_DIR", env)
        self.assertEqual(env["HOME"], str(self.home))
        r = subprocess.run(["bash", str(SCRIPT)], capture_output=True, text=True, env=env)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("SKIP", r.stdout)
        self.assertIn(str(self.home / "Developer" / "inkisle-rest"), r.stdout)
        self.assertEqual([p.name for p in self.home.iterdir()], [])
        self.assertTrue((self.clone / "content/queue/01-next-one").is_dir())  # the fixture clone was not touched either

    def test_script_itself_never_writes_a_log_file(self):
        # Logging is the launchd plist's job (StandardOutPath); the script only echoes. A test run must leave HOME empty.
        self.assertEqual(self.run_script().returncode, 0)
        # Only files count: macOS developer tools (the git/xcrun shim) may create an empty Library/ skeleton or a tool cache in a fresh HOME
        # (seen when the disk was full) — that is not the script logging, so Library/Caches and bare directories are ignored.
        written = [str(f.relative_to(self.home)) for f in self.home.rglob("*")
                   if f.is_file() and "Library/Caches" not in f.relative_to(self.home).as_posix()]
        self.assertEqual(written, [])

    def head(self, cwd=None):
        return git(cwd or self.clone, "rev-parse", "HEAD").stdout.strip()

    def origin_head(self):
        return git(self.origin, "rev-parse", "main").stdout.strip()

    def test_publishes_and_pushes_only_the_publish_set(self):
        r = self.run_script()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(self.head(), self.origin_head())
        self.assertTrue((self.clone / "content/journal/next-one/en.md").is_file())
        self.assertFalse((self.clone / "content/queue/01-next-one").exists())
        self.assertIn("journal: publish next-one", git(self.clone, "log", "-1", "--format=%s").stdout)
        self.assertEqual(git(self.clone, "status", "--porcelain").stdout, "")

    def test_second_run_same_day_is_a_noop(self):
        self.run_script()
        before = self.origin_head()
        r = self.run_script()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(self.origin_head(), before)

    def test_skips_when_not_on_main(self):
        git(self.clone, "checkout", "-q", "-b", "feature/x")
        before = self.head()
        r = self.run_script()
        self.assertEqual(r.returncode, 0)
        self.assertIn("SKIP", r.stdout)
        self.assertEqual(self.head(), before)
        self.assertEqual(self.origin_head(), before)
        self.assertTrue((self.clone / "content/queue/01-next-one").is_dir())

    def test_skips_when_tree_is_dirty(self):
        (self.clone / "wip.txt").write_text("work in progress")
        r = self.run_script()
        self.assertEqual(r.returncode, 0)
        self.assertIn("SKIP", r.stdout)
        self.assertTrue((self.clone / "content/queue/01-next-one").is_dir())
        self.assertEqual(git(self.clone, "log", "--oneline").stdout.count("\n"), 1)

    def kit_stubs(self, synced_ok):
        """A kit check that fails until the sync stub has run (marker file), and a sync stub that succeeds or fails."""
        marker = self.tmp / "kit-synced"
        return dict(INKISLE_KIT_CHECK_CMD="test -e '%s'" % marker,
                    INKISLE_KIT_SYNC_CMD=("touch '%s'; echo synced-stub" % marker) if synced_ok else "echo 'kit install failed: no tag v9' >&2; exit 1")

    def test_kit_mismatch_is_resynced_before_publishing(self):
        # Regression 11-08: the lock moved to v0.2.3 but vendor/ stayed v0.1.1 -> build_site ImportError -> no post that day.
        r = self.run_script(**self.kit_stubs(synced_ok=True))
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("syncing", r.stdout)
        self.assertIn("kit re-synced", r.stdout)
        self.assertTrue((self.clone / "content/journal/next-one/en.md").is_file())

    def test_kit_mismatch_that_cannot_be_synced_fails_loudly_and_touches_nothing(self):
        before = self.head()
        r = self.run_script(**self.kit_stubs(synced_ok=False))
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("KIT_MISMATCH", r.stdout)
        self.assertIn("no tag v9", r.stdout)
        self.assertEqual(self.head(), before)
        self.assertEqual(git(self.clone, "status", "--porcelain").stdout, "")
        self.assertTrue((self.clone / "content/queue/01-next-one").is_dir())
        self.assertFalse((self.clone / "content/journal/next-one").exists())

    def test_matching_kit_is_not_resynced(self):
        r = self.run_script(INKISLE_KIT_SYNC_CMD="echo SYNC-RAN; exit 1")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertNotIn("SYNC-RAN", r.stdout)

    def test_failed_green_gate_rolls_back_the_queue_move(self):
        before = self.head()
        r = self.run_script(check_cmd="false")
        self.assertEqual(r.returncode, 1)
        self.assertIn("ROLLBACK", r.stdout)
        self.assertEqual(self.head(), before)
        self.assertEqual(git(self.clone, "status", "--porcelain").stdout, "")
        self.assertTrue((self.clone / "content/queue/01-next-one").is_dir())
        self.assertFalse((self.clone / "content/journal/next-one").exists())
        # no stamp left behind: the next run (gate green again) publishes the same post today
        r = self.run_script()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertTrue((self.clone / "content/journal/next-one/en.md").is_file())

    def test_failed_build_rolls_back(self):
        q = self.clone / "content/queue/01-next-one/en.md"
        q.write_text(q.read_text().replace("Body of", "See /Users/someone/secret. Body of"), encoding="utf-8")
        git(self.clone, "commit", "-qam", "bad post")
        git(self.clone, "push", "-q", "origin", "main")
        before = self.head()
        r = self.run_script()
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertEqual(self.head(), before)
        self.assertEqual(git(self.clone, "status", "--porcelain").stdout, "")
        self.assertTrue((self.clone / "content/queue/01-next-one").is_dir())

    def test_unexpected_path_aborts_and_rolls_back(self):
        # a check command that drops a stray file simulates something touching the tree outside the publish set
        r = self.run_script(check_cmd="echo stray > stray.txt")
        self.assertEqual(r.returncode, 1)
        self.assertIn("unexpected paths", r.stdout)
        self.assertFalse((self.clone / "stray.txt").exists())
        self.assertTrue((self.clone / "content/queue/01-next-one").is_dir())

    def test_publish_paths_cover_exactly_the_site_languages(self):
        # Regression 11-13: the language set moved to 12 (pt-BR, zh-Hant, th, vi, tr) but PUBLISH_PATHS still listed the old dirs, so a publish that
        # rebuilt pt-BR/ was rolled back as "unexpected paths". The guard stays strict: stale dirs (zh, ru, pt) must NOT be allowed.
        import re
        import build_site as bs
        m = re.search(r'^PUBLISH_PATHS="([^"]*)"', SCRIPT.read_text(encoding="utf-8"), re.M)
        self.assertIsNotNone(m)
        paths = set(m.group(1).split())
        langs = {l for l in bs.LANGS if l != "en"}
        self.assertEqual(len(bs.LANGS), 12)
        self.assertTrue(langs <= paths, "language dirs missing from PUBLISH_PATHS: %s" % sorted(langs - paths))
        fixed = {"content/journal", "content/queue", "index.html", "404.html", "sitemap.xml", "llms.txt", "robots.txt", "journal"}
        self.assertEqual(paths - fixed, langs, "PUBLISH_PATHS has dirs that are not site languages")

    def test_commit_failure_rolls_back_the_staged_tree(self):
        hook = self.clone / ".git" / "hooks" / "pre-commit"
        hook.write_text("#!/bin/sh\nexit 1\n")
        hook.chmod(0o755)
        before = self.head()
        r = self.run_script()
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("ROLLBACK", r.stdout)
        self.assertEqual(self.head(), before)
        self.assertEqual(git(self.clone, "status", "--porcelain").stdout, "")
        self.assertTrue((self.clone / "content/queue/01-next-one").is_dir())
        hook.unlink()
        r = self.run_script()  # not stuck: the next run publishes normally
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertTrue((self.clone / "content/journal/next-one/en.md").is_file())

    def test_sigterm_during_the_gate_rolls_back(self):
        before = self.head()
        r = self.run_script(check_cmd="kill -TERM $PPID")
        self.assertEqual(r.returncode, 143, r.stdout + r.stderr)
        self.assertIn("ROLLBACK", r.stdout)
        self.assertEqual(self.head(), before)
        self.assertEqual(git(self.clone, "status", "--porcelain").stdout, "")
        self.assertTrue((self.clone / "content/queue/01-next-one").is_dir())

    def test_second_run_while_locked_is_skipped_and_the_lock_is_released_after_a_run(self):
        lock = self.clone / ".git" / "publish.lock"
        lock.mkdir()
        (lock / "pid").write_text(str(os.getpid()))  # a live process
        before = self.head()
        r = self.run_script()
        self.assertEqual(r.returncode, 0)
        self.assertIn("another publish run is in progress", r.stdout)
        self.assertTrue((self.clone / "content/queue/01-next-one").is_dir())
        self.assertEqual(self.head(), before)
        self.assertTrue(lock.is_dir())  # not ours: untouched
        shutil.rmtree(lock)
        r = self.run_script()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertFalse(lock.exists())

    def test_stale_lock_of_a_dead_process_is_taken_over(self):
        dead = subprocess.Popen(["true"])
        dead.wait()
        lock = self.clone / ".git" / "publish.lock"
        lock.mkdir()
        (lock / "pid").write_text(str(dead.pid))
        r = self.run_script()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("stale lock", r.stdout)
        self.assertTrue((self.clone / "content/journal/next-one/en.md").is_file())
        self.assertFalse(lock.exists())

    def test_lock_is_released_after_a_failed_run(self):
        self.run_script(check_cmd="false")
        self.assertFalse((self.clone / ".git" / "publish.lock").exists())

    def test_git_never_prompts_for_credentials(self):
        out = self.tmp / "env.txt"
        r = self.run_script(check_cmd='echo "$GIT_TERMINAL_PROMPT" > %s' % out)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(out.read_text().strip(), "0")

    def test_empty_queue_warns_loudly_and_exits_zero(self):
        shutil.rmtree(self.clone / "content" / "queue")
        git(self.clone, "add", "-A")
        git(self.clone, "commit", "-qm", "queue consumed")
        git(self.clone, "push", "-q", "origin", "main")
        r = self.run_script()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("QUEUE_EMPTY", r.stdout)
        self.assertEqual(git(self.clone, "status", "--porcelain").stdout, "")

    def test_low_queue_is_logged_with_the_count(self):
        r = self.run_script()  # fixture queues 2 posts
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("QUEUE_LOW 2", r.stdout)

    def test_comfortable_queue_is_not_flagged(self):
        q = self.clone / "content" / "queue"
        for n in (3, 4):
            d = q / ("0%d-extra-%d" % (n, n))
            d.mkdir()
            for lang in ("en", "ko"):
                (d / (lang + ".md")).write_text(helpers.post_text("extra-%d" % n, lang, "Queued extra %d %s" % (n, lang)), encoding="utf-8")
        git(self.clone, "add", "-A")
        git(self.clone, "commit", "-qm", "more queue")
        git(self.clone, "push", "-q", "origin", "main")
        r = self.run_script()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertNotIn("QUEUE_LOW", r.stdout)

    def test_unpushed_commit_outside_the_publish_set_is_not_pushed(self):
        (self.clone / "wip.txt").write_text("not for publication")
        git(self.clone, "add", "wip.txt")
        git(self.clone, "commit", "-qm", "wip")
        before = self.origin_head()
        r = self.run_script()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("WARN", r.stdout)
        self.assertIn("wip.txt", r.stdout)
        # 11-19: the stray commit is kept on a backup branch and the day's post still goes out, without the wip file
        self.assertIn("backup/stray-", git(self.clone, "branch", "--list", "backup/stray-*").stdout)
        self.assertNotEqual(self.origin_head(), before)
        self.assertNotIn("wip.txt", git(self.clone, "ls-tree", "-r", "--name-only", "origin/main").stdout)
        self.assertFalse((self.clone / "content/queue/01-next-one").is_dir())

    def test_diverged_unpushed_commit_is_skipped_before_any_rebase(self):
        # 10-31: a release-notes commit made in the publish clone collided with origin; it must be skipped untouched, never rebased
        (self.clone / "notes.txt").write_text("local")
        git(self.clone, "add", "-A")
        git(self.clone, "commit", "-qm", "local notes")
        other = self.tmp / "other"
        git(self.tmp, "clone", "-q", str(self.origin), str(other))
        (other / "notes.txt").write_text("remote")
        git(other, "add", "-A")
        git(other, "commit", "-qm", "remote notes")
        git(other, "push", "-q", "origin", "main")
        head, before = self.head(), self.origin_head()
        r = self.run_script()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("WARN", r.stdout)
        self.assertIn("notes.txt", r.stdout)
        self.assertIn(head, git(self.clone, "branch", "--list", "backup/stray-*", "--format=%(objectname)").stdout)  # local commit kept, never rebased
        self.assertFalse((self.clone / ".git" / "rebase-merge").exists())

    def test_failing_rollback_is_logged_loudly_and_still_releases_the_lock(self):
        # an index.lock makes `git reset --hard` fail, simulating a rollback that cannot complete
        r = self.run_script(check_cmd="touch .git/index.lock; false")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("ROLLBACK FAILED", r.stdout)
        self.assertFalse((self.clone / ".git" / "publish.lock").exists())
        # same through the EXIT trap (error after the gate, e.g. SIGTERM)
        (self.clone / ".git" / "index.lock").unlink()
        git(self.clone, "reset", "-q", "--hard")
        git(self.clone, "clean", "-fdq")
        r = self.run_script(check_cmd="touch .git/index.lock; kill -TERM $PPID")
        self.assertEqual(r.returncode, 143, r.stdout + r.stderr)
        self.assertIn("ROLLBACK FAILED", r.stdout)
        self.assertFalse((self.clone / ".git" / "publish.lock").exists())

    def test_failed_push_is_retried_by_the_next_run_even_with_nothing_to_publish(self):
        hook = self.origin / "hooks" / "pre-receive"
        hook.write_text("#!/bin/sh\nexit 1\n")
        hook.chmod(0o755)
        r = self.run_script()
        self.assertEqual(r.returncode, 1)
        self.assertIn("commit kept locally", r.stdout)
        ahead = git(self.clone, "rev-list", "--count", "origin/main..HEAD").stdout.strip()
        self.assertEqual(ahead, "1")
        hook.unlink()
        r = self.run_script()  # today already has a post: nothing new, but the leftover commit goes out
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("unpushed", r.stdout)
        self.assertEqual(self.head(), self.origin_head())

    def test_not_a_clone_is_skipped(self):
        r = self.run_script(publish_dir=self.tmp)
        self.assertEqual(r.returncode, 0)
        self.assertIn("SKIP", r.stdout)


class PublishPages(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory(prefix="inkisle-pages-")
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        self.addCleanup(os.chdir, Path.cwd())
        os.chdir(root)
        self.lock = root / ".git" / "publish.lock"
        self.lock.mkdir(parents=True)
        self.url = "https://inkisle.ipe.rest/journal/test-post/"
        post = Path("journal/test-post/index.html")
        post.parent.mkdir(parents=True)
        post.touch()
        self.pending = publish_pages.PENDING

    def test_pending_urls_expire_at_exactly_72_hours(self):
        now = dt.datetime(2026, 11, 25, 12, tzinfo=publish_pages.KST)
        recorded_at = int(now.timestamp()) - 3 * 24 * 60 * 60 + 1
        expiry = now + dt.timedelta(seconds=1)
        with mock.patch.object(publish_pages.dt, "datetime", wraps=dt.datetime) as clock, \
             mock.patch.object(publish_pages, "pages_are_live", return_value=False) as probe, \
             mock.patch.object(publish_pages.subprocess, "run") as submit:
            for pages_live in (False, True):
                with self.subTest(pages_live=pages_live):
                    entry = {"recorded_at": recorded_at, "pages_live": pages_live, "last_submit_day": "2026-11-25"}
                    self.pending.write_text(json.dumps({self.url: entry}))
                    clock.now.return_value = now
                    self.assertEqual(publish_pages.verify(self.lock), 0 if pages_live else 1)
                    self.assertEqual(json.loads(self.pending.read_text()), {self.url: entry})
                    probe.reset_mock()

                    clock.now.return_value = expiry
                    self.assertEqual(publish_pages.verify(self.lock), 0)
                    self.assertFalse(self.pending.exists())
                    probe.assert_not_called()
            submit.assert_not_called()

    def assert_retries_indexnow_next_kst_day(self, failure):
        now = dt.datetime(2026, 11, 25, 23, 59, 58, tzinfo=publish_pages.KST)
        same_day = now + dt.timedelta(seconds=1)
        next_day = now + dt.timedelta(seconds=2)
        self.pending.write_text(json.dumps({self.url: {"recorded_at": int(now.timestamp()), "pages_live": True}}))
        success = subprocess.CompletedProcess([], 0, stdout="", stderr="")
        with mock.patch.object(publish_pages.dt, "datetime", wraps=dt.datetime) as clock, \
             mock.patch.object(publish_pages, "pages_are_live") as probe, \
             mock.patch.object(publish_pages.subprocess, "run", side_effect=[failure, success]) as submit:
            clock.now.return_value = now
            self.assertEqual(publish_pages.verify(self.lock), 0)
            clock.now.assert_called_with(publish_pages.KST)
            self.assertEqual(json.loads(self.pending.read_text())[self.url]["last_submit_day"], "2026-11-25")
            self.assertEqual(submit.call_count, 1)

            clock.now.return_value = same_day
            self.assertEqual(publish_pages.verify(self.lock), 0)
            self.assertEqual(submit.call_count, 1)

            clock.now.return_value = next_day
            self.assertEqual(publish_pages.verify(self.lock), 0)
            self.assertEqual(submit.call_count, 2)
            self.assertFalse(self.pending.exists())
            probe.assert_not_called()

    def test_indexnow_network_error_is_retried_on_next_kst_day(self):
        failure = subprocess.CompletedProcess([], 1, stdout="", stderr="URLError: timed out\n")
        self.assert_retries_indexnow_next_kst_day(failure)

    def test_indexnow_rate_limit_is_retried_on_next_kst_day(self):
        failure = subprocess.CompletedProcess([], 1, stdout="IndexNow inkisle.ipe.rest: HTTP 429 (3 URLs)\n", stderr="")
        self.assert_retries_indexnow_next_kst_day(failure)


class OpsFiles(unittest.TestCase):
    def test_deploy_workflow_settings(self):
        y = (REPO / ".github" / "workflows" / "deploy.yml").read_text(encoding="utf-8")
        self.assertIn("cancel-in-progress: false", y)
        self.assertNotIn("cancel-in-progress: true", y)
        check = y.split("  check:")[1].split("  deploy:")[0]
        self.assertIn("permissions:\n      contents: read", check)

    def test_plist_template_has_no_personal_paths_and_renders(self):
        t = (REPO / "ops" / "rest.ipe.inkisle-publish.plist.template").read_text(encoding="utf-8")
        self.assertNotIn("/Users/", t)
        self.assertIn("<key>Hour</key><integer>12</integer><key>Minute</key><integer>0</integer>", t)  # slot ticks 12:00-18:45 -> slot_gate.sh
        self.assertIn("ops/slot_gate.sh", t)
        self.assertIn("__HOME__/Library/Logs/inkisle-publish.log", t)
        self.assertIn("INKISLE_PUBLISH_DIR", t)
        self.assertIn("<key>GIT_TERMINAL_PROMPT</key><string>0</string>", t)
        tmp = Path(tempfile.mkdtemp(prefix="inkisle-ld-"))
        self.addCleanup(shutil.rmtree, tmp, True)
        env = helpers.isolated_env(tmp / "hm", INKISLE_LAUNCH_AGENTS_DIR=str(tmp / "LA"), INKISLE_HOME=str(tmp / "home"))
        r = subprocess.run(["bash", str(REPO / "ops" / "install_launchd.sh")], capture_output=True, text=True, env=env)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        out = (tmp / "LA" / "rest.ipe.inkisle-publish.plist").read_text(encoding="utf-8")
        self.assertNotIn("__HOME__", out)
        self.assertIn(str(tmp / "home" / "Library" / "Logs" / "inkisle-publish.log"), out)
        self.assertIn(str(tmp / "home" / "Developer" / "inkisle-rest" / "ops" / "slot_gate.sh"), out)
        if shutil.which("plutil"):
            self.assertEqual(subprocess.run(["plutil", "-lint", str(tmp / "LA" / "rest.ipe.inkisle-publish.plist")], capture_output=True).returncode, 0)

    def test_install_rejects_unsafe_home_values(self):
        tmp = Path(tempfile.mkdtemp(prefix="inkisle-ld-"))
        self.addCleanup(shutil.rmtree, tmp, True)
        for bad in ("relative/home", "/a\\b", "/a\nb", "/a#b", "/a&b", "/a|b", ""):
            env = helpers.isolated_env(tmp / "hm", INKISLE_LAUNCH_AGENTS_DIR=str(tmp / "LA"), INKISLE_HOME=bad)
            if bad == "":
                env.pop("INKISLE_HOME")
                env["HOME"] = "relative"  # (never the real home: the guard must reject before anything is written)
            r = subprocess.run(["bash", str(REPO / "ops" / "install_launchd.sh")], capture_output=True, text=True, env=env)
            self.assertEqual(r.returncode, 1, (bad, r.stdout, r.stderr))
            self.assertIn("HOME", r.stderr, bad)  # rejected by our own check, not by a later failure
            self.assertFalse((tmp / "LA" / "rest.ipe.inkisle-publish.plist").exists(), bad)

    def test_template_comment_does_not_contain_the_placeholder(self):
        t = (REPO / "ops" / "rest.ipe.inkisle-publish.plist.template").read_text(encoding="utf-8")
        comment = t.split("<!--")[1].split("-->")[0]
        self.assertNotIn("__HOME__", comment)

    def test_no_personal_absolute_paths_in_the_repo(self):
        """Public repo: no /Users/<name>/ or /home/<name>/ anywhere except files that deliberately name the forbidden string."""
        import re
        pat = re.compile(r"/(Users|home)/[A-Za-z0-9._-]+/")
        skip_dirs = {".git", "__pycache__", "node_modules"}
        allowed = {"docs/TRANSLATION.md", "scripts/build_site.py"}
        bad = []
        for p in REPO.rglob("*"):
            rel = p.relative_to(REPO)
            if not p.is_file() or skip_dirs & set(rel.parts) or rel.parts[0] == "tests" or rel.as_posix() in allowed:
                continue
            if p.suffix in (".png", ".jpg", ".jpeg", ".ico"):
                continue
            try:
                text = p.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            if pat.search(text):
                bad.append(rel.as_posix())
        self.assertEqual(bad, [])


if __name__ == "__main__":
    unittest.main()
