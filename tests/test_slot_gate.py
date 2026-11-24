"""ops/slot_gate.py: random afternoon slot (12:00-17:59 KST, never the same hour as yesterday), state file, publish gating."""
import json
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

import helpers
from helpers import REPO

SCRIPT = REPO / "ops" / "slot_gate.sh"


class SlotGate(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="inkisle-slot-"))
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.slot = self.tmp / "q" / "slot.json"
        self.calls = self.tmp / "calls"

    def run_gate(self, now, publish="echo 'publish_daily: pushed some-slug'"):
        cmd = "echo x >> %s; %s" % (self.calls, publish)
        env = helpers.isolated_env(self.tmp / "home", INKISLE_SLOT_FILE=str(self.slot), INKISLE_NOW=now, INKISLE_PUBLISH_CMD=cmd)
        return subprocess.run(["bash", str(SCRIPT)], capture_output=True, text=True, env=env)

    def state(self):
        return json.loads(self.slot.read_text())

    def n_calls(self):
        return len(self.calls.read_text().split()) if self.calls.exists() else 0

    def write(self, **kw):
        self.slot.parent.mkdir(parents=True, exist_ok=True)
        self.slot.write_text(json.dumps(kw))

    def test_draw_in_range_and_never_yesterdays_hour(self):
        for i in range(24):
            prev_hour = 12 + i % 6
            self.write(date="2026-11-12", time="%02d:%02d" % (prev_hour, i % 60), published=True)
            r = self.run_gate("2026-11-13 08:00")           # before any slot: only draws
            self.assertEqual(r.returncode, 0, r.stderr)
            t = self.state()["time"]
            h, m = int(t[:2]), int(t[3:])
            self.assertTrue(12 <= h <= 17 and 0 <= m <= 59, t)
            self.assertNotEqual(h, prev_hour)

    def test_date_rollover_moves_current_to_prev(self):
        self.write(date="2026-11-12", time="14:20", published=True)
        self.run_gate("2026-11-13 09:00")
        s = self.state()
        self.assertEqual((s["date"], s["prev_date"], s["prev_time"], s["published"]), ("2026-11-13", "2026-11-12", "14:20", False))
        self.assertNotEqual(s["time"][:2], "14")
        self.assertEqual(self.n_calls(), 0)

    def test_first_run_without_state_file(self):
        self.run_gate("2026-11-13 09:00")
        s = self.state()
        self.assertEqual((s["date"], s["prev_time"], s["published"]), ("2026-11-13", None, False))

    def test_no_publish_before_slot_time(self):
        self.write(date="2026-11-13", time="15:30", published=False)
        self.run_gate("2026-11-13 15:29")
        self.assertEqual(self.n_calls(), 0)
        self.run_gate("2026-11-13 15:30")
        self.assertEqual(self.n_calls(), 1)
        self.assertTrue(self.state()["published"])

    def test_already_published_is_ignored(self):
        self.write(date="2026-11-13", time="13:00", published=True)
        self.run_gate("2026-11-13 16:00")
        self.assertEqual(self.n_calls(), 0)

    def test_skip_queue_empty_and_failure_keep_false_and_retry(self):
        for out in ("echo 'publish_daily: SKIP — working tree is not clean'", "echo 'publish_daily: QUEUE_EMPTY — x'", "echo boom; exit 1"):
            self.write(date="2026-11-13", time="13:00", published=False)
            self.run_gate("2026-11-13 13:15", publish=out)
            self.assertFalse(self.state()["published"], out)
        self.write(date="2026-11-13", time="13:00", published=False)
        self.run_gate("2026-11-13 13:30", publish="echo 'publish_daily: nothing to publish'")
        self.assertTrue(self.state()["published"])

    def test_pending_pages_keeps_slot_open_until_verification_even_with_an_empty_queue(self):
        self.write(date="2026-11-13", time="13:00", published=False)
        first = self.run_gate(
            "2026-11-13 13:00",
            publish="echo 'publish_daily: pushed some-slug'; echo 'publish_daily: FAIL — PAGES_NOT_LIVE'; exit 1",
        )
        self.assertFalse(self.state()["published"])
        self.assertIn("push complete — Pages verification pending", first.stdout)
        pending = self.run_gate(
            "2026-11-13 13:15",
            publish="echo 'publish_daily: QUEUE_EMPTY'; echo 'publish_daily: FAIL — PAGES_NOT_LIVE'; exit 1",
        )
        self.assertFalse(self.state()["published"])
        self.assertIn("earlier push — Pages verification pending", pending.stdout)
        self.run_gate(
            "2026-11-13 13:30",
            publish="echo 'publish_daily: QUEUE_EMPTY'; echo 'publish_daily: Pages follow-up complete'",
        )
        self.assertTrue(self.state()["published"])
        self.assertEqual(self.n_calls(), 3)

    def test_indexnow_pending_does_not_keep_slot_open(self):
        self.write(date="2026-11-13", time="13:00", published=False)
        result = self.run_gate(
            "2026-11-13 13:00",
            publish="echo 'publish_daily: WARN — INDEXNOW_PENDING'; echo 'publish_daily: Pages follow-up complete'",
        )
        self.assertIn("slot done", result.stdout)
        self.assertTrue(self.state()["published"])
        self.run_gate("2026-11-13 13:15")
        self.assertEqual(self.n_calls(), 1)

    def test_successful_retry_of_earlier_push_completes_slot(self):
        self.write(date="2026-11-13", time="13:00", published=False)
        result = self.run_gate("2026-11-13 13:00", publish="echo 'publish_daily: pushed earlier publication commit(s)'")
        self.assertIn("slot done", result.stdout)
        self.assertTrue(self.state()["published"])

    def test_hard_cutoff_at_1800(self):
        self.write(date="2026-11-13", time="13:00", published=False)
        self.run_gate("2026-11-13 18:00")
        self.assertEqual(self.n_calls(), 0)
        self.run_gate("2026-11-13 18:01")
        self.assertEqual(self.n_calls(), 0)
        self.assertFalse(self.state()["published"])
        self.run_gate("2026-11-13 17:59")
        self.assertEqual(self.n_calls(), 1)
        self.assertTrue(self.state()["published"])

    def test_unpublished_1759_publishes(self):
        self.write(date="2026-11-13", time="17:29", published=False)
        self.run_gate("2026-11-13 17:59")
        self.assertEqual(self.n_calls(), 1)

    def test_draw_leaves_two_ticks_before_1800(self):
        import random, sys
        sys.path.insert(0, str(REPO / "ops"))
        import slot_gate
        rng = random.Random(7)
        for i in range(2000):
            prev = "%02d:%02d" % (12 + i % 6, i % 60)
            t = slot_gate.draw(prev, rng)
            h, m = int(t[:2]), int(t[3:])
            self.assertTrue(12 <= h <= 17 and 0 <= m <= 59, t)
            self.assertNotEqual(h, int(prev[:2]))
            first = ((h * 60 + m + 14) // 15) * 15          # first 15-min tick at/after the slot
            ticks = [x for x in range(first, 18 * 60, 15)]
            self.assertGreaterEqual(len(ticks), 2, t)
            if h == 17:
                self.assertLessEqual(m, 29)

    def test_no_publish_at_1801_when_slot_already_published(self):
        """5cc3111 incident guard: today's slot (e.g. 17:19) already published -> 18:01 must not publish again."""
        self.write(date="2026-11-20", time="17:19", published=True)
        self.run_gate("2026-11-20 18:01")
        self.assertEqual(self.n_calls(), 0)

    def test_no_publish_at_1917_even_if_unpublished(self):
        """Past the 18:00 cutoff: never publishes, state stays unpublished, uses a marker command (no real push)."""
        self.write(date="2026-11-20", time="16:58", published=False)
        r = self.run_gate("2026-11-20 19:17")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(self.n_calls(), 0)
        self.assertFalse(self.state()["published"])

    def test_new_day_slot_is_always_before_1800(self):
        for i in range(30):
            self.write(date="2026-11-19", time="16:58", published=True)
            self.run_gate("2026-11-20 12:00")
            self.assertLess(self.state()["time"], "18:00")

    def test_plist_template_has_the_afternoon_ticks(self):
        text = (REPO / "ops" / "rest.ipe.inkisle-publish.plist.template").read_text()
        self.assertIn("ops/slot_gate.sh", text)
        self.assertEqual(text.count("<key>Hour</key>"), 28)
        self.assertNotIn("<integer>19</integer>", text)


if __name__ == "__main__":
    unittest.main()
