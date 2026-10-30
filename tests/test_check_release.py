import contextlib
import io
import json
import shutil
import unittest
from pathlib import Path

from helpers import REPO, bs, build, make_site

import check_release as cr  # noqa: E402


def entry(n, langs=tuple(bs.LANGS), notes=2):
    mk = lambda f: {l: f(l) for l in langs}  # noqa: E731
    return {"id": "1.0.0-%d" % n, "version": "1.0.0", "build": str(n), "status": "testflight", "date": "2026-10-30",
            "title": mk(lambda l: "T%d %s" % (n, l)), "intro": mk(lambda l: "I%d %s" % (n, l)),
            "notes": mk(lambda l: ["n%d %s %d" % (n, l, i) for i in range(notes)])}


class CheckRelease(unittest.TestCase):
    def site(self, *entries):
        root = make_site(langs=tuple(bs.LANGS))
        self.addCleanup(shutil.rmtree, root, True)
        (root / "content" / "releases.json").write_text(json.dumps({"releases": list(entries)}), encoding="utf-8")
        build(root)
        return root

    def test_complete_entry_passes(self):
        root = self.site(entry(7), entry(6))
        self.assertEqual(cr.check(root, "7"), [])
        self.assertEqual(cr.check(root, "1.0.0+6"), [])

    def test_unknown_build(self):
        errs = cr.check(self.site(entry(6)), "7")
        self.assertEqual(len(errs), 1)
        self.assertIn("build 7: no entry", errs[0])

    def test_missing_languages_are_named(self):
        root = self.site(entry(7, langs=("en", "ko", "ja")))
        errs = cr.check(root, "7")
        text = "\n".join(errs)
        for field in ("title", "intro", "notes"):
            for lang in ("zh", "es", "fr", "de", "pt", "ru", "ar", "hi", "id"):
                self.assertIn("%s.%s" % (field, lang), text)
        self.assertNotIn("title.ja", text)

    def test_note_count_must_match_english(self):
        e = entry(7)
        e["notes"]["de"] = e["notes"]["de"][:1]
        errs = cr.check(self.site(e), "7")
        self.assertTrue(any("notes.de has 1 items, en has 2" in x for x in errs), errs)

    def test_stale_generated_page(self):
        root = self.site(entry(6))
        data = json.loads((root / "content" / "releases.json").read_text(encoding="utf-8"))
        data["releases"].insert(0, entry(7))
        (root / "content" / "releases.json").write_text(json.dumps(data), encoding="utf-8")
        errs = cr.check(root, "7")
        self.assertEqual(len(errs), 12)
        self.assertTrue(all("stale" in x for x in errs))
        self.assertEqual(cr.check(root, "7", pages=False), [])
        build(root)
        self.assertEqual(cr.check(root, "7"), [])

    def test_bad_argument(self):
        self.assertIn("--build must be", cr.check(self.site(entry(6)), "seven")[0])

    def test_cli_exit_codes(self):
        root = self.site(entry(6))
        with contextlib.redirect_stdout(io.StringIO()) as out:
            self.assertEqual(cr.main(["--root", str(root), "--build", "6"]), 0)
            self.assertEqual(cr.main(["--root", str(root), "--build", "7"]), 1)
        self.assertIn("NOT ready", out.getvalue())

    def test_repo_notes_complete_for_every_listed_build(self):
        # the real releases.json: every entry already in it must be complete in all 12 languages
        data = json.loads((REPO / "content" / "releases.json").read_text(encoding="utf-8"))
        for e in data["releases"]:
            if e.get("build") in ("6", "7"):
                self.assertEqual(cr.check(REPO, e["build"], pages=False), [], e["id"])


if __name__ == "__main__":
    unittest.main()
