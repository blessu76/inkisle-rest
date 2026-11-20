"""GA4: one snippet per generated page, and the privacy text in all 12 languages that must match it."""
import json
import re
import shutil
import subprocess
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
        for rel in ("assets/inkisle.js", "assets/inkisle.css", "assets/ipe-lang.js"):
            self.assertNotIn(GA_ID, (REPO / rel).read_text(encoding="utf-8"))

    def test_committed_pages_have_it(self):
        for rel in ("index.html", "404.html", "privacy/index.html", "ko/index.html", "ja/privacy/index.html", "th/privacy/index.html"):
            with self.subTest(rel):
                self.assertEqual((REPO / rel).read_text(encoding="utf-8").count(GA_ID), 1)

    def test_privacy_matches_the_tracking_in_all_12_languages(self):
        for lang in bs.LANGS:
            src = (REPO / "content" / "pages" / lang / "privacy.md").read_text(encoding="utf-8")
            with self.subTest(lang):
                for needle in ("Google", "_ga", OPT_OUT, "ink-theme", "ipe_lang"):
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

    def test_hostname_guard_comes_before_loader_and_config_in_every_page(self):
        # structure, not just presence: the local-host return must precede the loader element and gtag('config') on every page
        for rel, text in self.pages.items():
            with self.subTest(rel):
                snip = self.inline_snippet(text)
                guard = snip.index("location.hostname")
                loader = snip.index("createElement('script')")
                config = snip.index("gtag('config',GA_ID)")
                self.assertLess(guard, loader)
                self.assertLess(loader, config)
                self.assertLess(snip.index("return;"), loader)

    @staticmethod
    def inline_snippet(page_text):
        m = re.search(r"<script>(\(function\(\)\{var h=location\.hostname;.*?)</script>", page_text, re.S)
        if not m:
            raise AssertionError("GA snippet with hostname guard not found")
        return m.group(1)

    def run_snippet(self, snippet, hostname):
        payload = json.dumps({"code": snippet, "hostname": hostname})
        proc = subprocess.run(["node", "-e", NODE_HARNESS], input=payload, capture_output=True, text=True, check=True)
        return json.loads(proc.stdout)

    @unittest.skipUnless(shutil.which("node"), "node not installed")
    def test_runtime_local_hosts_send_nothing(self):
        snippet = self.inline_snippet(self.pages["index.html"])
        for host in ("localhost", "127.0.0.1", "[::1]", "0.0.0.0", ""):
            with self.subTest(host=host):
                out = self.run_snippet(snippet, host)
                self.assertEqual(out["appended"], [])
                self.assertEqual(out["dataLayer"], [])
                self.assertEqual(out["clickListeners"], [])

    @unittest.skipUnless(shutil.which("node"), "node not installed")
    def test_runtime_live_host_loads_loader_then_configs(self):
        snippet = self.inline_snippet(self.pages["index.html"])
        out = self.run_snippet(snippet, "inkisle.ipe.rest")
        self.assertEqual(len(out["appended"]), 1)
        self.assertEqual(out["appended"][0]["src"], "https://www.googletagmanager.com/gtag/js?id=" + GA_ID)
        self.assertTrue(out["appended"][0]["async"])
        names = [call[0] for call in out["dataLayer"]]
        self.assertEqual(names[:2], ["js", "config"])
        self.assertEqual(out["dataLayer"][1][1], GA_ID)
        self.assertEqual(out["clickListeners"], ["click", "auxclick"])


NODE_HARNESS = r"""
let input = '';
process.stdin.on('data', d => input += d).on('end', () => {
  const { code, hostname } = JSON.parse(input);
  const appended = [], listeners = {};
  global.location = { hostname };
  global.document = {
    head: { appendChild: e => appended.push(e) },
    createElement: tag => ({ tag }),
    addEventListener: (type) => { listeners[type] = true; },
  };
  global.window = global;
  new Function(code)();
  const dataLayer = (global.dataLayer || []).map(a => Array.from(a).map(v => (v instanceof Date ? 'date' : v)));
  console.log(JSON.stringify({
    appended: appended.map(e => ({ tag: e.tag, async: e.async, src: e.src })),
    dataLayer,
    clickListeners: Object.keys(listeners),
  }));
});
"""


if __name__ == "__main__":
    unittest.main()
