"""GEO checks on the real content: JSON-LD, FAQPage, sitemap, feed, llms.txt and robots for AI bots."""
import datetime as dt
import json
import re
import unittest

from helpers import REPO, bs

NOW = dt.datetime(2026, 12, 31, 12, 0, tzinfo=bs.KST)
LD = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)


class Geo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ctx, errs = bs.make_ctx(REPO, NOW)
        assert not errs, errs
        cls.files = bs.build_all(cls.ctx)
        slugs = {p["slug"] for p in cls.ctx.posts}
        cls.post_pages = {k: v for k, v in cls.files.items() if any(k.endswith("journal/%s/index.html" % s) for s in slugs)}

    def test_journal_posts_exist(self):
        self.assertGreaterEqual(len(self.post_pages), 18)

    def test_every_jsonld_block_parses(self):
        for name, text in self.files.items():
            if not name.endswith(".html"):
                continue
            blocks = LD.findall(text)
            for b in blocks:
                data = json.loads(b)
                self.assertTrue(data.get("@context") or data.get("@graph"), name)
        for name, text in self.post_pages.items():
            types = {n["@type"] for b in LD.findall(text) for n in json.loads(b).get("@graph", [])}
            self.assertTrue({"BlogPosting", "BreadcrumbList", "VideoGame"} <= types, (name, types))

    def test_game_about_fields(self):
        g = bs.game_ld("en", self.ctx)
        self.assertEqual(g["gamePlatform"], ["iOS"])
        self.assertIn("Strategy", g["genre"])
        self.assertEqual(g["name"], "Inkisle")

    def test_faq_posts_emit_valid_faqpage(self):
        n = 0
        for name, text in self.post_pages.items():
            graph = [x for b in LD.findall(text) for x in json.loads(b)["@graph"]]
            faq = [x for x in graph if x["@type"] == "FAQPage"]
            if not faq:
                continue
            n += 1
            qs = faq[0]["mainEntity"]
            self.assertGreaterEqual(len(qs), 2, name)
            for q in qs:
                self.assertEqual(q["@type"], "Question")
                self.assertTrue(q["name"].strip() and q["acceptedAnswer"]["text"].strip(), name)
        self.assertGreaterEqual(n, 36)  # 18 posts x (en, ko)

    def test_english_posts_all_have_faq(self):
        for name, text in self.post_pages.items():
            if not name.startswith(("ko/", "de/", "es/", "fr/", "id/", "ja/", "pt-BR/")):
                self.assertIn("FAQPage", text, name)

    def test_faq_items_parser(self):
        body = "Intro.\n\n## FAQ\n\n### Q one?\n\nAnswer **one**.\n\n### Q two?\n\nAnswer [two](/x).\n\n## Other\n\ntext\n"
        self.assertEqual(bs.faq_items(body), [("Q one?", "Answer one."), ("Q two?", "Answer two.")])
        self.assertEqual(bs.faq_items("## Other\n\n### Q?\n\nA.\n"), [])

    def test_post_meta_unique_and_linked(self):
        titles, descs = set(), set()
        for name, text in self.post_pages.items():
            if name.startswith(("ko/", "de/", "es/", "fr/", "id/", "ja/", "pt-BR/")):
                continue
            t = re.search(r"<title>(.*?)</title>", text).group(1)
            d = re.search(r'<meta name="description" content="(.*?)"', text).group(1)
            self.assertNotIn(t, titles)
            self.assertNotIn(d, descs)
            titles.add(t)
            descs.add(d)
            self.assertIn('rel="canonical"', text)
            self.assertIn('hreflang="x-default"', text)
            self.assertIn('name="twitter:card"', text)
            self.assertIn('href="/journal/"', text)

    def test_sitemap_lists_journal(self):
        sm = self.files["sitemap.xml"]
        self.assertIn("https://inkisle.ipe.rest/journal/", sm)
        for p in self.ctx.posts:
            self.assertIn("https://inkisle.ipe.rest/journal/%s/" % p["slug"], sm)

    def test_feed(self):
        feed = self.files[bs.path_feed("en").lstrip("/")]
        self.assertIn("<rss", feed)
        for p in self.ctx.posts:
            self.assertIn("/journal/%s/" % p["slug"], feed)

    def test_llms_lists_journal(self):
        llms = self.files["llms.txt"]
        self.assertIn("/journal/", llms)
        for p in self.ctx.posts:
            self.assertIn("https://inkisle.ipe.rest/journal/%s/" % p["slug"], llms)

    def test_robots_allows_ai_bots(self):
        robots = self.files["robots.txt"]
        self.assertIn("Sitemap:", robots)
        for bot in ("GPTBot", "ClaudeBot", "PerplexityBot"):
            self.assertIn(bot, bs.BOTS)
        blocks = re.split(r"\n\s*\n", robots)
        for b in blocks:
            if re.search(r"User-agent:\s*(\*|GPTBot|ClaudeBot|PerplexityBot)", b):
                self.assertNotRegex(b, r"Disallow:\s*/\s*$")

    def test_queue_posts_are_geo_shaped(self):
        qdir = REPO / "content" / "queue"
        for d in sorted(qdir.glob("*/")):
            for lang in ("en", "ko"):
                body = (d / (lang + ".md")).read_text(encoding="utf-8").split("---", 2)[2]
                self.assertGreaterEqual(len(bs.faq_items(body)), 2, d.name + "/" + lang)
                self.assertIn("iOS", body)


if __name__ == "__main__":
    unittest.main()
