"""Community (comments) wiring: community.json drives the private kit's `community` module. OFF = nothing changes in the output."""
import json
import re
import shutil
import sys
import unittest
from pathlib import Path

from helpers import NOW, REPO, bs, make_site

sys.path.insert(0, str(REPO / "vendor"))  # the private kit, installed by scripts/kit_lock.py

ON = {"siteId": "inkisle.ipe.rest", "features": {"comments": True, "likes": False, "reports": False}}


def write_cfg(root, cfg):
    (Path(root) / "community.json").write_text(json.dumps(cfg), encoding="utf-8")


def read_all(root):
    return {str(f.relative_to(root)): f.read_text(encoding="utf-8") for f in Path(root).rglob("*.html")}


class Committed(unittest.TestCase):
    def test_config_is_inkisle_and_loads(self):
        from ipe_web_kit import community
        cm = community.load(REPO / "community.json")
        self.assertEqual(cm.site_id, "inkisle.ipe.rest")
        self.assertEqual(cm.langs, list(bs.LANGS))  # same 12 languages as the site (the server rules accept only these)

    def test_not_published_by_the_pages_workflow(self):
        self.assertIn("--exclude='community.json'", (REPO / ".github/workflows/deploy.yml").read_text(encoding="utf-8"))


class Switch(unittest.TestCase):
    def setUp(self):
        self.root = make_site()
        self.addCleanup(shutil.rmtree, self.root, True)

    def built(self):
        ctx, errs = bs.make_ctx(self.root, now=NOW)
        self.assertEqual(errs, [])
        return ctx, bs.build_all(ctx)

    def test_missing_file_and_all_false_change_nothing(self):
        _, base = self.built()
        write_cfg(self.root, {"siteId": "inkisle.ipe.rest"})
        _, off = self.built()
        self.assertEqual(base, off)
        for rel, text in off.items():
            self.assertNotIn("ipe-cm", text, rel)
            self.assertNotIn("ipe-community", text, rel)
            self.assertNotIn("firestore", text, rel)

    def test_on_adds_the_widget_to_posts_only(self):
        write_cfg(self.root, ON)
        _, files = self.built()
        for rel, text in files.items():
            if not rel.endswith(".html"):
                continue
            is_post = re.match(r"^(?:[a-z]{2}/)?journal/[a-z0-9-]+/index\.html$", rel) and "/page/" not in rel
            with self.subTest(rel):
                if is_post:
                    self.assertEqual(text.count('<section class="ipe-cm"'), 1)
                    self.assertIn('data-site="inkisle.ipe.rest"', text)
                    self.assertIn('data-features="comments"', text)
                    self.assertRegex(text, r'href="/assets/ipe-community\.css\?v=[\w-]+"')
                    self.assertRegex(text, r'src="/assets/ipe-community\.js\?v=[\w-]+" defer')
                    self.assertIn('id="ipe-theme"', text)
                else:
                    self.assertNotIn("ipe-cm", text)
                    self.assertNotIn("ipe-community", text)

    def test_one_thread_per_post_across_languages(self):
        write_cfg(self.root, ON)
        _, files = self.built()
        en = re.search(r'data-post="([^"]+)"', files["journal/alpha-post/index.html"]).group(1)
        ko = re.search(r'data-post="([^"]+)"', files["ko/journal/alpha-post/index.html"]).group(1)
        self.assertEqual(en, ko)
        self.assertIn('data-lang="ko"', files["ko/journal/alpha-post/index.html"])

    def test_placeholder_firebase_stops_the_build(self):
        write_cfg(self.root, dict(ON, firebase={"projectId": "REPLACE", "apiKey": "REPLACE"}))
        with self.assertRaises(ValueError):
            bs.make_ctx(self.root, now=NOW)

    def test_main_copies_the_assets_only_when_on(self):
        self.assertEqual(bs.main(["--root", str(self.root)]), 0)
        self.assertFalse((self.root / "assets" / "ipe-community.js").exists())
        write_cfg(self.root, ON)
        self.assertEqual(bs.main(["--root", str(self.root)]), 0)
        self.assertTrue((self.root / "assets" / "ipe-community.js").is_file())
        self.assertTrue((self.root / "assets" / "ipe-community.css").is_file())


if __name__ == "__main__":
    unittest.main()
