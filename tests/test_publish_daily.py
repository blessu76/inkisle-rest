"""ops/publish_daily.sh safety rules, run against a throw-away origin + publish clone (no network, no real check.sh)."""
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

import helpers
from helpers import REPO

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
        helpers.build(site)
        self.tmp = Path(tempfile.mkdtemp(prefix="inkisle-pd-"))
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.origin = self.tmp / "origin.git"
        git(self.tmp, "init", "-q", "--bare", "-b", "main", str(self.origin))
        self.clone = site
        git(site, "init", "-q", "-b", "main")
        git(site, "add", "-A")
        git(site, "commit", "-q", "-m", "init")
        git(site, "remote", "add", "origin", str(self.origin))
        git(site, "push", "-q", "origin", "main")
        self.check_cmd = "true"

    def run_script(self, check_cmd=None, publish_dir=None):
        env = {**os.environ, "INKISLE_PUBLISH_DIR": str(publish_dir or self.clone), "INKISLE_CHECK_CMD": check_cmd or self.check_cmd,
               "INKISLE_SKIP_NET": "1", "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t", "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t"}
        return subprocess.run(["bash", str(SCRIPT)], capture_output=True, text=True, env=env)

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


class OpsFiles(unittest.TestCase):
    def test_deploy_workflow_settings(self):
        y = (REPO / ".github" / "workflows" / "deploy.yml").read_text(encoding="utf-8")
        self.assertIn("cancel-in-progress: false", y)
        self.assertNotIn("cancel-in-progress: true", y)
        check = y.split("  check:")[1].split("  deploy:")[0]
        self.assertIn("permissions:\n      contents: read", check)

    def test_plist(self):
        p = (REPO / "ops" / "rest.ipe.inkisle-publish.plist").read_text(encoding="utf-8")
        self.assertIn("<key>Hour</key><integer>19</integer>", p)
        self.assertIn("Library/Logs/inkisle-publish.log", p)
        self.assertIn("INKISLE_PUBLISH_DIR", p)
        if shutil.which("plutil"):
            self.assertEqual(subprocess.run(["plutil", "-lint", str(REPO / "ops" / "rest.ipe.inkisle-publish.plist")], capture_output=True).returncode, 0)


if __name__ == "__main__":
    unittest.main()
