"""Community (comments) wiring: community.json drives the private kit's `community` module. OFF = nothing changes in the output."""
import json
import re
import shutil
import sys
import unittest
from pathlib import Path

from helpers import NOW, REPO, bs, make_site

sys.path.insert(0, str(REPO / "vendor"))  # the private kit, installed by scripts/kit_lock.py

ON = {"siteId": "inkisle.ipe.rest", "enabled": True}


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


PRIVACY = REPO / "content" / "community" / "privacy"
PLACEHOLDERS = {"{{RETENTION_YEARS}}", "{{HIDDEN_DELETE_DAYS}}", "{{DELETE_REQUEST_DAYS}}", "{{MIN_AGE}}"}
VALUES = {"RETENTION_YEARS": 3, "HIDDEN_DELETE_DAYS": 90, "DELETE_REQUEST_DAYS": 30, "MIN_AGE": 14}


class PrivacyText(unittest.TestCase):
    """content/community/privacy/<lang>.md: the comments section of the privacy policy, shown only once comments are ON."""

    def test_every_language_has_it_with_the_same_undecided_values(self):
        for lang in bs.LANGS:
            text = (PRIVACY / (lang + ".md")).read_text(encoding="utf-8")
            with self.subTest(lang):
                self.assertEqual(set(re.findall(r"\{\{[A-Z_]+\}\}", text)), PLACEHOLDERS)
                self.assertEqual(len(re.findall(r"^\*\*", text, re.M)), 7)  # same structure in every language
                self.assertIn("ipe.haven@gmail.com", text)
                self.assertNotRegex(text, r"\[(?:결정|검토)")  # internal review markers never ship
                if lang != "ko":
                    self.assertNotRegex(text, r"[가-힣]")

    def test_the_site_ships_with_the_widget_off(self):
        self.assertFalse(json.loads((REPO / "community.json").read_text(encoding="utf-8"))["enabled"])


class Switch(unittest.TestCase):
    def setUp(self):
        self.root = make_site()
        self.addCleanup(shutil.rmtree, self.root, True)
        shutil.copytree(PRIVACY, self.root / "content" / "community" / "privacy")
        old = dict(bs.COMMUNITY_PRIVACY_VALUES)  # the owner has not decided these yet; tests of the ON state use example values
        bs.COMMUNITY_PRIVACY_VALUES.update(VALUES)
        self.addCleanup(lambda: (bs.COMMUNITY_PRIVACY_VALUES.clear(), bs.COMMUNITY_PRIVACY_VALUES.update(old)))

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
                    self.assertIn('data-features="comments likes reports"', text)
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

    def test_privacy_comments_section_only_when_on(self):
        _, off = self.built()
        for rel, anchor in (("privacy/index.html", "Comments and likes"), ("ko/privacy/index.html", "댓글과 좋아요")):
            self.assertNotIn(anchor, off[rel])

    def test_on_stops_the_build_while_a_privacy_value_is_undecided(self):
        write_cfg(self.root, ON)
        bs.COMMUNITY_PRIVACY_VALUES.pop("MIN_AGE")
        with self.assertRaisesRegex(ValueError, r"\{\{MIN_AGE\}\}"):
            self.built()

    def test_privacy_comments_section_goes_before_the_app_section(self):
        write_cfg(self.root, ON)
        files = self.built()[1]
        for rel, anchor, app in (("privacy/index.html", "Comments and likes", "2. The App"), ("ko/privacy/index.html", "댓글과 좋아요", "2. 앱")):
            with self.subTest(rel):
                page = files[rel]
                self.assertEqual(page.count("ipe.haven@gmail.com"), 3)  # contact line + "Your choices" + the comments deletion paragraph
                self.assertNotIn("{{", page)
                self.assertLess(page.index(anchor), page.index(app))

    def test_main_copies_the_assets_only_when_on(self):
        for name in ("ipe-community.css", "ipe-community.js"):  # make_site copies the repo's assets, which hold them once the site is ON
            if (self.root / "assets" / name).exists():
                (self.root / "assets" / name).unlink()
        self.assertEqual(bs.main(["--root", str(self.root)]), 0)
        self.assertFalse((self.root / "assets" / "ipe-community.js").exists())
        write_cfg(self.root, ON)
        self.assertEqual(bs.main(["--root", str(self.root)]), 0)
        self.assertTrue((self.root / "assets" / "ipe-community.js").is_file())
        self.assertTrue((self.root / "assets" / "ipe-community.css").is_file())


if __name__ == "__main__":
    unittest.main()
