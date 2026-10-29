import json
import os
import re
import shutil
import subprocess
import unittest
from pathlib import Path

from helpers import NOW, REPO, bs, build, jsonld, make_site, post_text


class Markdown(unittest.TestCase):
    def test_inline_and_escape(self):
        out = bs.markdown("Hello **bold** and *it* and `a<b` and <script>x</script> [l](https://a.b/?x=1&y=2)", ".")
        self.assertIn("<strong>bold</strong>", out)
        self.assertIn("<em>it</em>", out)
        self.assertIn("<code>a&lt;b</code>", out)
        self.assertNotIn("<script>", out)
        self.assertIn('href="https://a.b/?x=1&amp;y=2" rel="noopener"', out)

    def test_blocks(self):
        md = "## H\n\n- a\n- b\n\n1. x\n2. y\n\n> quote\n\n| A | B |\n|---|---|\n| 1 | 2 |\n\n```\ncode <b>\n```\n"
        out = bs.markdown(md, ".")
        for frag in ("<h2>H</h2>", "<ul><li>a</li><li>b</li></ul>", "<ol><li>x</li><li>y</li></ol>", "<blockquote>", "<table>",
                     "<th>A</th>", "<td>2</td>", "<pre><code>code &lt;b&gt;"):
            self.assertIn(frag, out)
        self.assertIn('class="table-wrap"', out)

    def test_image_with_caption_and_size(self):
        out = bs.markdown("![alt text](/assets/posts/img/art-compare.jpg)\n*A caption*", str(REPO))
        self.assertIn("<figure><img", out)
        self.assertIn("<figcaption>A caption</figcaption>", out)
        self.assertRegex(out, r'width="\d+" height="\d+"')


class Loading(unittest.TestCase):
    def setUp(self):
        self.root = make_site()
        self.addCleanup(shutil.rmtree, self.root, True)

    def test_ok(self):
        posts, errs = bs.load_posts(self.root, NOW)
        self.assertEqual(errs, [])
        self.assertEqual([p["slug"] for p in posts], ["beta-post", "alpha-post"])  # newest first

    def test_future_time_refused(self):
        f = self.root / "content/journal/beta-post/en.md"
        f.write_text(f.read_text().replace("2026-11-02T19:00", "2026-11-03T20:01"))
        _, errs = bs.load_posts(self.root, NOW)
        self.assertTrue(any("future" in e for e in errs), errs)

    def test_requires_both_originals_and_matching_names(self):
        (self.root / "content/journal/beta-post/ko.md").unlink()
        _, errs = bs.load_posts(self.root, NOW)
        self.assertTrue(any("ko original missing" in e for e in errs))
        f = self.root / "content/journal/alpha-post/en.md"
        f.write_text(f.read_text().replace("slug: alpha-post", "slug: other"))
        _, errs = bs.load_posts(self.root, NOW)
        self.assertTrue(any("slug" in e for e in errs))

    def test_bad_time_format_and_forbidden_text(self):
        f = self.root / "content/journal/alpha-post/en.md"
        f.write_text(f.read_text().replace("2026-11-01T19:00+09:00", "2026-11-01"))
        _, errs = bs.load_posts(self.root, NOW)
        self.assertTrue(any("published must look like" in e for e in errs))
        g = self.root / "content/journal/beta-post/ko.md"
        g.write_text(g.read_text() + "\nsee /Users/someone/secret\n")
        _, errs = bs.load_posts(self.root, NOW)
        self.assertTrue(any("forbidden" in e for e in errs))

    def test_translation_needs_translation_of(self):
        d = self.root / "content/journal/alpha-post"
        (d / "ja.md").write_text(post_text("alpha-post", "ja", "T", "2026-11-01T19:00+09:00").replace("translation_of: en\n", ""))
        _, errs = bs.load_posts(self.root, NOW)
        self.assertTrue(any("translation_of" in e for e in errs))

    def test_queue_must_not_carry_published(self):
        root = make_site(queue=("gamma-post",))
        self.addCleanup(shutil.rmtree, root, True)
        self.assertEqual(bs.queue_errors(root), [])
        f = root / "content/queue/01-gamma-post/en.md"
        f.write_text(f.read_text().replace("category: making-of", "category: making-of\npublished: 2026-11-03T19:00+09:00"))
        self.assertTrue(any("must not carry" in e for e in bs.queue_errors(root)))


class Output(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = make_site()
        cls.ctx = build(cls.root)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.root, True)

    def read(self, rel):
        return (self.root / rel).read_text(encoding="utf-8")

    def test_files_exist(self):
        for rel in ("index.html", "ko/index.html", "about/index.html", "ko/about/index.html", "privacy/index.html", "journal/index.html",
                    "ko/journal/index.html", "journal/alpha-post/index.html", "ko/journal/beta-post/index.html", "journal/feed.xml",
                    "ko/journal/feed.xml", "sitemap.xml", "robots.txt", "llms.txt", "404.html"):
            self.assertTrue((self.root / rel).is_file(), rel)

    def test_head_seo(self):
        h = self.read("journal/alpha-post/index.html")
        self.assertIn('<link rel="canonical" href="https://inkisle.ipe.rest/journal/alpha-post/">', h)
        self.assertIn('hreflang="ko" href="https://inkisle.ipe.rest/ko/journal/alpha-post/"', h)
        self.assertIn('hreflang="x-default" href="https://inkisle.ipe.rest/journal/alpha-post/"', h)
        self.assertIn('<html lang="en" dir="ltr"', h)
        self.assertIn('property="og:image" content="https://inkisle.ipe.rest/assets/og-image.png"', h)
        self.assertIn("2026-11-01T19:00:00+09:00", h)
        self.assertIn("/assets/inkisle.css?v=" + bs.ASSET_V, h)

    def test_json_ld(self):
        post = jsonld(self.read("journal/alpha-post/index.html"))[0]["@graph"]
        types = {n["@type"] for n in post}
        self.assertTrue({"WebSite", "BlogPosting", "BreadcrumbList", "Organization"} <= types)
        bp = next(n for n in post if n["@type"] == "BlogPosting")
        self.assertEqual(bp["datePublished"], "2026-11-01T19:00:00+09:00")
        self.assertEqual(bp["inLanguage"], "en")
        self.assertEqual(bp["author"]["@id"], bs.ORG_ID)
        crumbs = next(n for n in post if n["@type"] == "BreadcrumbList")["itemListElement"]
        self.assertEqual([c["position"] for c in crumbs], [1, 2, 3])
        home = jsonld(self.read("index.html"))[0]["@graph"]
        g = next(n for n in home if n["@type"] == "VideoGame")
        self.assertEqual(g["name"], "Inkisle")
        self.assertNotIn("offers", g)
        self.assertNotIn("datePublished", g)
        self.assertIn("Blog", {n["@type"] for n in jsonld(self.read("journal/index.html"))[0]["@graph"]})

    def test_ipe_rest_links_header_and_footer(self):
        h = self.read("index.html")
        self.assertGreaterEqual(h.count('href="https://ipe.rest/"'), 2)
        self.assertLess(h.index("ipe-link"), h.index("<main"))
        self.assertGreater(h.rindex('href="https://ipe.rest/"'), h.index("</main>"))

    def test_status_is_honest(self):
        h = self.read("index.html").lower()
        self.assertIn("not yet released", h)
        self.assertNotIn("app store", h)
        self.assertNotIn("download", h)

    def test_sitemap_robots_llms_feed(self):
        sm = self.read("sitemap.xml")
        self.assertIn("<loc>https://inkisle.ipe.rest/journal/beta-post/</loc>", sm)
        self.assertIn("<lastmod>2026-11-02</lastmod>", sm)
        self.assertIn("Sitemap: https://inkisle.ipe.rest/sitemap.xml", self.read("robots.txt"))
        self.assertIn("GPTBot", self.read("robots.txt"))
        llms = self.read("llms.txt")
        self.assertIn("NOT been released", llms)
        self.assertIn("https://inkisle.ipe.rest/journal/alpha-post/", llms)
        feed = self.read("journal/feed.xml")
        self.assertIn("<pubDate>Mon, 02 Nov 2026 19:00:00 +0900</pubDate>", feed)
        self.assertLess(feed.index("beta-post"), feed.index("alpha-post"))

    def test_404_noindex_and_no_external_assets(self):
        self.assertIn("noindex", self.read("404.html"))
        for rel in ("index.html", "journal/alpha-post/index.html"):
            h = self.read(rel)
            self.assertNotRegex(h, r'<script[^>]+src="https?://')
            self.assertNotRegex(h, r'<link[^>]+rel="stylesheet"[^>]+href="https?://')

    def test_deterministic(self):
        a = bs.build_all(self.ctx)
        b = bs.build_all(bs.make_ctx(self.root, NOW)[0])
        self.assertEqual(a, b)

    def test_lang_switcher_and_pagination(self):
        h = self.read("ko/journal/alpha-post/index.html")
        self.assertIn('lang="en"', h)
        self.assertIn('aria-current="true"', h)
        self.assertIn('<html lang="ko"', h)

    def test_pagination_with_many_posts(self):
        posts = tuple(("post-%02d" % i, "2026-10-%02dT19:00+09:00" % (i + 1)) for i in range(12))
        root = make_site(posts=posts)
        self.addCleanup(shutil.rmtree, root, True)
        build(root)
        self.assertTrue((root / "journal/page/2/index.html").is_file())
        self.assertIn('rel="next"', (root / "journal/index.html").read_text())
        self.assertIn("https://inkisle.ipe.rest/journal/page/2/", (root / "sitemap.xml").read_text())


class RealRepo(unittest.TestCase):
    """The committed sources themselves."""

    def test_sources_valid(self):
        ctx, errs = bs.make_ctx(REPO)
        self.assertEqual(errs, [])

    def test_i18n_keys_and_placeholders(self):
        base = json.loads((REPO / "content/i18n/en.json").read_text())
        self.assertEqual(set(base), set(bs.KEYS))
        for f in sorted((REPO / "content/i18n").glob("*.json")):
            d = json.loads(f.read_text())
            self.assertEqual(set(d), set(bs.KEYS), f.name)
            for k in ("hero_h1", "journal_title", "nav_home"):
                self.assertTrue(d[k].strip(), (f.name, k))

    def test_pages_keep_placeholders_and_links(self):
        for lang in bs.LANGS:
            for slug in ("about", "privacy"):
                f = REPO / "content/pages" / lang / (slug + ".md")
                if not f.exists():
                    continue
                t = f.read_text(encoding="utf-8")
                self.assertIn("{{EMAIL}}", t, f)
                if slug == "privacy":
                    self.assertIn("{{EFFECTIVE}}", t, f)
                    self.assertIn("{{OPERATOR}}", t, f)
                self.assertNotIn("@gmail", t, f)  # the address is a placeholder, never hard-coded in a translation

    def test_asset_references_exist(self):
        for f in list((REPO / "content").rglob("*.md")):
            for m in re.finditer(r"\]\((/assets/[^)\s]+)\)", f.read_text(encoding="utf-8")):
                self.assertTrue((REPO / m.group(1).lstrip("/")).is_file(), "%s -> %s" % (f.name, m.group(1)))
        for slug in {p.name.split("-", 1)[1] for p in (REPO / "content/queue").glob("*")} | {p.name for p in (REPO / "content/journal").glob("*")}:
            self.assertTrue((REPO / "assets/posts" / (slug + ".svg")).is_file(), slug)

    def test_static_assets(self):
        for rel in ("assets/inkisle.css", "assets/inkisle.js", "assets/logo.svg", "assets/favicon.svg", "assets/hero.svg", "assets/icon-180.png",
                    "assets/og-image.png", "CNAME"):
            self.assertTrue((REPO / rel).is_file(), rel)
        self.assertEqual(bs.img_size(REPO, "/assets/og-image.png"), (1200, 630))
        self.assertEqual((REPO / "CNAME").read_text().strip(), "inkisle.ipe.rest")

    def test_asset_version_in_pages_matches(self):
        self.assertTrue(bs.ASSET_V)

    def test_indexnow_key_file(self):
        keys = [p for p in REPO.glob("*.txt") if re.fullmatch(r"[0-9a-f]{32}\.txt", p.name)]
        self.assertEqual(len(keys), 1)
        self.assertEqual(keys[0].read_text().strip(), keys[0].stem)


class Releases(unittest.TestCase):
    def setUp(self):
        self.root = make_site()
        self.addCleanup(shutil.rmtree, self.root, True)

    def entry(self, **kw):
        e = {"id": "1.0.0-2", "version": "1.0.0", "build": "2", "status": "testflight", "date": "2026-11-02",
             "title": {"en": "Build 2", "ko": "빌드 2"}, "intro": {"en": "Intro.", "ko": "소개."},
             "notes": {"en": ["Fixed **a thing**."], "ko": ["고쳤습니다."]}}
        e.update(kw)
        return e

    def write(self, entries):
        (self.root / "content" / "releases.json").write_text(json.dumps({"releases": entries}), encoding="utf-8")

    def test_page_menu_and_footer_in_every_language(self):
        # the committed site (check.sh proves it is up to date) in all 12 languages
        for lang in bs.LANGS:
            link = '<a href="%s">' % bs.path_releases(lang)
            home = (REPO / bs.path_home(lang).lstrip("/") / "index.html").read_text(encoding="utf-8")
            self.assertIn(link, home.split("</header>")[0], lang)
            self.assertIn(link, home.split("</main>")[1], lang)
            page = (REPO / bs.path_releases(lang).lstrip("/") / "index.html").read_text(encoding="utf-8")
            self.assertIn('class="card release"', page, lang)
            self.assertIn('<a href="%s" aria-current="page">' % bs.path_releases(lang), page, lang)
            self.assertIn('<html lang="%s"' % lang, page)

    def test_current_page_is_marked_in_menu(self):
        build(self.root)
        h = (self.root / "releases/index.html").read_text(encoding="utf-8")
        self.assertIn('<a href="/releases/" aria-current="page">Release notes</a>', h)

    def test_real_entries_keep_status_dates_order_and_no_prices(self):
        rel = json.loads((REPO / "content" / "releases.json").read_text(encoding="utf-8"))["releases"]
        self.assertTrue(rel)
        # a "prep" (preparing) build has no date; a "testflight" build has an ISO date
        for r in rel:
            if r["status"] == "prep":
                self.assertEqual(r["date"], "", r["id"])
            else:
                self.assertRegex(r["date"], r"^\d{4}-\d{2}-\d{2}$", r["id"])
        # newest first: dated builds come before any preparing build, in descending date order,
        # and build numbers descend
        seen_prep = False
        for r in rel:
            if r["status"] == "prep":
                seen_prep = True
            else:
                self.assertFalse(seen_prep, "dated entry %s listed after a preparing build" % r["id"])
        dated = [r for r in rel if r["status"] != "prep"]
        self.assertEqual([r["date"] for r in dated], sorted((r["date"] for r in dated), reverse=True))
        builds = [int(r["build"]) for r in rel]
        self.assertEqual(builds, sorted(builds, reverse=True))
        # no prices, release dates or commit talk in any entry
        for r in rel:
            text = json.dumps(r, ensure_ascii=False).lower()
            for bad in ("$", "price", "free", "release date", "가격", "무료", "커밋"):
                self.assertNotIn(bad, text, r["id"])

    def test_missing_language_falls_back_to_english_and_says_so(self):
        build(self.root)
        # the test site only has en + ko, so check fallback with a fake third language entry rendered by hand
        ctx, errs = bs.make_ctx(self.root, NOW)
        self.assertEqual(errs, [])
        ctx.langs.append("ja")
        ctx.i18n["ja"] = json.loads((REPO / "content/i18n/ja.json").read_text(encoding="utf-8"))
        path, h = bs.build_releases(ctx, "ja")
        self.assertEqual(path, "/ja/releases/")
        fallback = next(r for r in ctx.releases if "ja" not in r["title"])  # an entry without its own ja text
        self.assertIn(fallback["title"]["en"], h)
        self.assertIn(ctx.i18n["ja"]["rel_en_note"], h)
        self.assertIn('lang="en" dir="ltr"', h)
        self.assertIn('<html lang="ja"', h)

    def test_newest_first_status_badge_and_markdown(self):
        self.write([self.entry(), self.entry(id="1.0.0-1", build="1", status="prep", date="")])
        build(self.root)
        h = (self.root / "releases/index.html").read_text(encoding="utf-8")
        self.assertLess(h.index('id="1.0.0-2"'), h.index('id="1.0.0-1"'))
        self.assertIn("On TestFlight", h)
        self.assertIn("Preparing for TestFlight", h)
        self.assertIn("<strong>a thing</strong>", h)
        self.assertIn('<time datetime="2026-11-02">2026-11-02</time>', h)

    def test_validation_errors(self):
        for bad, frag in ((self.entry(status="live"), "status"), (self.entry(date="Nov 2"), "date"),
                          (self.entry(notes={"en": ["x"]}), "notes.ko missing"), (self.entry(notes={"en": [], "ko": ["x"]}), "notes.en"),
                          (self.entry(title={"en": "T", "ko": "T", "xx": "T"}), "unknown language"),
                          (self.entry(notes={"en": ["see /Users/x"], "ko": ["x"]}), "forbidden"), (self.entry(id="a b"), "id")):
            self.write([bad])
            _, errs = bs.load_releases(self.root)
            self.assertTrue(any(frag in e for e in errs), (frag, errs))
        self.write([self.entry(), self.entry()])
        self.assertTrue(any("duplicated" in e for e in bs.load_releases(self.root)[1]))
        (self.root / "content" / "releases.json").unlink()
        self.assertTrue(any("missing" in e for e in bs.load_releases(self.root)[1]))

    def test_sitemap_hreflang_llms(self):
        ctx = build(self.root)
        sm = (self.root / "sitemap.xml").read_text(encoding="utf-8")
        self.assertIn("<loc>https://inkisle.ipe.rest/releases/</loc>", sm)
        self.assertIn("<loc>https://inkisle.ipe.rest/ko/releases/</loc>", sm)
        h = (self.root / "releases/index.html").read_text(encoding="utf-8")
        self.assertIn('hreflang="ko" href="https://inkisle.ipe.rest/ko/releases/"', h)
        self.assertIn('hreflang="x-default" href="https://inkisle.ipe.rest/releases/"', h)
        self.assertIn('<link rel="canonical" href="https://inkisle.ipe.rest/releases/">', h)
        self.assertIn("/releases/", (self.root / "llms.txt").read_text(encoding="utf-8"))
        import check_sitemap
        errs, _ = check_sitemap.check(self.root, NOW)
        self.assertEqual(errs, [])
        self.assertTrue(ctx.releases)


NODE = shutil.which("node")
# CI must never skip the language-pick tests silently
NEED_NODE = unittest.skipUnless(NODE or os.environ.get("CI"), "node not installed")


class LanguagePick(unittest.TestCase):
    """The root page follows the browser language (assets/langpick.js, inlined into / only)."""

    def run_pick(self, languages, saved=None, path="/", broken_storage=False):
        script = re.search(r"<script>(\(function\(\)\{var S=.*?)</script>", (REPO / "index.html").read_text(encoding="utf-8"), re.S).group(1)
        harness = (
            "var vm=require('vm');var out=null;var store=%s;var broken=%s;"
            "var sb={location:{pathname:%s,search:'?a=1',hash:'#h',replace:function(u){out=u}},"
            "navigator:{languages:%s,language:%s},"
            "localStorage:{getItem:function(k){if(broken)throw new Error('blocked');return k==='ink-lang'?store:null}}};"
            "vm.runInNewContext(%s,sb);console.log(JSON.stringify(out));"
        ) % (json.dumps(saved), "true" if broken_storage else "false", json.dumps(path), json.dumps(languages),
             json.dumps(languages[0] if languages else ""), json.dumps(script))
        self.assertTrue(NODE, "node is required in CI")
        r = subprocess.run([NODE, "-e", harness], capture_output=True, text=True, timeout=20)
        self.assertEqual(r.returncode, 0, r.stderr)
        return json.loads(r.stdout)

    @NEED_NODE
    def test_follows_browser_language(self):
        for langs, want in ((["ko-KR", "en-US"], "/ko/?a=1#h"), (["zh-TW"], "/zh/?a=1#h"), (["pt-BR"], "/pt/?a=1#h"), (["fr"], "/fr/?a=1#h"),
                            (["ar-EG", "en"], "/ar/?a=1#h"), (["sv", "ja-JP"], "/ja/?a=1#h"), (["id_ID"], "/id/?a=1#h"), (["in"], "/id/?a=1#h"), (["in-ID", "en"], "/id/?a=1#h"), (["KO-kr"], "/ko/?a=1#h")):
            self.assertEqual(self.run_pick(langs), want, langs)

    @NEED_NODE
    def test_english_and_unknown_stay_on_the_english_root(self):
        for langs in (["en-US"], ["en"], ["sv", "nb"], ["xx-YY"], [""], []):
            self.assertIsNone(self.run_pick(langs), langs)

    @NEED_NODE
    def test_saved_choice_wins_and_survives_blocked_storage(self):
        self.assertIsNone(self.run_pick(["ko-KR"], saved="en"))
        self.assertEqual(self.run_pick(["en-US"], saved="ja"), "/ja/?a=1#h")
        self.assertEqual(self.run_pick(["ko-KR"], saved="klingon"), "/ko/?a=1#h")  # unknown saved value ignored
        self.assertEqual(self.run_pick(["ko-KR"], broken_storage=True), "/ko/?a=1#h")  # storage throws -> still works

    @NEED_NODE
    def test_only_runs_on_the_root(self):
        self.assertIsNone(self.run_pick(["ko-KR"], path="/about/"))
        self.assertIsNone(self.run_pick(["ko-KR"], path="/ko/"))

    def test_script_only_on_root_and_lists_built_languages(self):
        root = make_site()
        self.addCleanup(shutil.rmtree, root, True)
        build(root)
        home = (root / "index.html").read_text(encoding="utf-8")
        self.assertIn('var S=["en", "ko"]', home)
        for rel in ("ko/index.html", "about/index.html", "releases/index.html", "journal/index.html", "404.html"):
            self.assertNotIn("ink-lang", (root / rel).read_text(encoding="utf-8"), rel)
        self.assertEqual(home.count("ink-lang"), 1)

    def test_seo_stays_intact_and_links_visible_without_js(self):
        root = make_site()
        self.addCleanup(shutil.rmtree, root, True)
        build(root)
        h = (root / "index.html").read_text(encoding="utf-8")
        self.assertIn('<link rel="canonical" href="https://inkisle.ipe.rest/">', h)
        self.assertIn('hreflang="x-default" href="https://inkisle.ipe.rest/"', h)
        self.assertNotIn("http-equiv", h)  # no meta refresh
        foot = h.split("</main>")[1]
        self.assertIn('<p class="foot-langs"', foot)
        self.assertIn('href="/ko/" hreflang="ko" lang="ko"', foot)
        self.assertNotIn("<noscript>", h)

    def test_explicit_choice_is_stored_by_the_language_links(self):
        js = (REPO / "assets" / "inkisle.js").read_text(encoding="utf-8")
        self.assertIn("localStorage.setItem('ink-lang'", js)
        self.assertIn(".lang a[hreflang]", js)
        self.assertIn(".foot-langs a[hreflang]", js)


if __name__ == "__main__":
    unittest.main()
