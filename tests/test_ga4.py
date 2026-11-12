"""GA4: one snippet per generated page, and the privacy text in all 12 languages that must match it."""
import re
import shutil
import unittest

from helpers import REPO, build, bs, make_site

GA_ID = "G-XG4BH800J0"
OPT_OUT = "https://tools.google.com/dlpage/gaoptout"


class Ga4(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = make_site()
        build(cls.root)
        cls.pages = {str(p.relative_to(cls.root)): p.read_text(encoding="utf-8") for p in cls.root.rglob("*.html")}

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.root, True)

    def test_constant_is_the_ipe_rest_property(self):
        self.assertEqual(bs.GA_MEASUREMENT_ID, GA_ID)

    def test_every_generated_page_has_the_snippet_once(self):
        self.assertGreater(len(self.pages), 8)
        self.assertIn("404.html", self.pages)
        for rel, text in self.pages.items():
            with self.subTest(rel):
                self.assertEqual(text.count("googletagmanager.com/gtag/js"), 1)
                self.assertEqual(text.count(GA_ID), 1)
                self.assertEqual(text.count("window.gtag('config',GA_ID)"), 1)
                self.assertLess(text.index(GA_ID), text.index("</body>"))

    def test_no_snippet_in_assets(self):
        for rel in ("assets/inkisle.js", "assets/inkisle.css", "assets/langpick.js"):
            self.assertNotIn(GA_ID, (REPO / rel).read_text(encoding="utf-8"))

    def test_committed_pages_have_it(self):
        for rel in ("index.html", "404.html", "privacy/index.html", "ko/index.html", "ja/privacy/index.html", "th/privacy/index.html"):
            with self.subTest(rel):
                self.assertEqual((REPO / rel).read_text(encoding="utf-8").count(GA_ID), 1)

    def test_privacy_matches_the_tracking_in_all_12_languages(self):
        for lang in bs.LANGS:
            src = (REPO / "content" / "pages" / lang / "privacy.md").read_text(encoding="utf-8")
            with self.subTest(lang):
                for needle in ("Google", "_ga", OPT_OUT, "ink-theme", "ink-lang"):
                    self.assertIn(needle, src)
                self.assertNotIn("Google Analytics 4 Google", src)

    def test_no_stale_no_analytics_claims(self):
        stale = re.compile(r"uses no analytics|sets no cookies|분석 도구를 쓰지 않|쿠키도 설정하지 않|Cookie も設定しません|不设置任何 Cookie", re.I)
        for lang in bs.LANGS:
            with self.subTest(lang):
                self.assertIsNone(stale.search((REPO / "content" / "pages" / lang / "privacy.md").read_text(encoding="utf-8")))
        self.assertIsNone(stale.search((REPO / "llms.txt").read_text(encoding="utf-8")))

    def test_privacy_mentions_icloud_sync_in_all_12_languages(self):
        for lang in bs.LANGS:
            with self.subTest(lang):
                self.assertIn("iCloud", (REPO / "content" / "pages" / lang / "privacy.md").read_text(encoding="utf-8"))

    def test_llms_txt_says_so(self):
        self.assertIn("Google Analytics", (REPO / "llms.txt").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
