"""Language picker: every built page shows a <select> with its own language selected and links that stay on the same page;
the kit's ipe-lang.js (loaded on "/" only) sends a first visit to the saved choice or the browser language."""
import json
import re
import shutil
import subprocess
import unittest

from helpers import REPO, bs

LANG_DIRS = [l for l in bs.LANGS if l != "en"]
SELECT = re.compile(r'<select class="ipe-lang__select"[^>]*>(.*?)</select>', re.S)
OPTION = re.compile(r'<option value="([^"]*)" lang="([\w-]+)"( selected)?>')


def pages():
    out = []
    for p in REPO.rglob("index.html"):
        rel = p.relative_to(REPO).parts
        if rel[0] in ("tests", "scripts", "docs", "ops", "content", "assets", "vendor"):
            continue
        lang = rel[0] if rel[0] in LANG_DIRS else "en"
        out.append((lang, str(p.relative_to(REPO)), p.read_text(encoding="utf-8")))
    return out


class Picker(unittest.TestCase):
    def test_all_twelve_languages_have_pages(self):
        self.assertEqual({l for l, _, _ in pages()}, set(bs.LANGS))

    def test_select_shows_the_pages_own_language(self):
        for lang, f, h in pages():
            self.assertEqual(re.search(r'<html lang="([\w-]+)"', h).group(1), lang, f)
            options = OPTION.findall(SELECT.search(h).group(1))
            selected = [l for _, l, sel in options if sel]
            self.assertEqual(selected, [lang], f)
            if "journal/" in f:  # a journal index offers only the languages that have posts
                self.assertTrue(1 <= len(options) <= len(bs.LANGS), f)
            else:
                self.assertEqual(len(options), len(bs.LANGS), f)

    def test_select_options_stay_on_the_same_page(self):
        for lang, f, h in pages():
            for href, l, _ in OPTION.findall(SELECT.search(h).group(1)):
                if l == "en":
                    self.assertFalse(href.startswith(tuple("/" + x + "/" for x in LANG_DIRS)), (f, href))
                else:
                    self.assertTrue(href.startswith("/" + l + "/"), (f, href))

    def test_only_the_root_runs_the_redirect(self):
        for lang, f, h in pages():
            tags = re.findall(r'<script src="/assets/ipe-lang\.js\?v=[^"]+"[^>]*></script>', h)
            self.assertEqual(len(tags), 1 if f == "index.html" else 0, f)
            if tags:
                self.assertIn("data-redirect", tags[0])


DETECT = r"""
var vm=require('vm');
var a=%s;
var sel={selectedIndex:0,options:a.options};
var sb={navigator:{userAgent:a.ua,languages:a.langs,language:(a.langs||[''])[0]},
  localStorage:{getItem:function(k){if(a.broken)throw new Error('blocked');return k==='ipe_lang'?a.saved:null}},
  location:{replace:function(u){sb.out=u}},
  document:{currentScript:{getAttribute:function(n){return a.redirect&&n==='data-redirect'?'':null}},
    getElementById:function(id){return id==='ipe-lang-select'?sel:null}}};
sb.window=sb;
vm.runInNewContext(%s,sb);
console.log(JSON.stringify(sb.out===undefined?null:sb.out));
"""

OPTIONS = [{"value": "/" if l == "en" else "/%s/" % l, "lang": l} for l in bs.LANGS]


class Detect(unittest.TestCase):
    def detect(self, langs, saved=None, redirect=True, ua="Mozilla/5.0", broken=False, options=OPTIONS):
        js = (REPO / "assets" / "ipe-lang.js").read_text(encoding="utf-8")
        args = {"options": options, "langs": langs, "saved": saved, "redirect": redirect, "ua": ua, "broken": broken}
        r = subprocess.run(["node", "-e", DETECT % (json.dumps(args), json.dumps(js))], capture_output=True, text=True, timeout=20)
        self.assertEqual(r.returncode, 0, r.stderr)
        return json.loads(r.stdout)

    @unittest.skipUnless(shutil.which("node"), "node required")
    def test_follows_browser_language(self):
        for langs, want in ((["ko-KR", "en-US"], "/ko/"), (["zh-TW"], "/zh-Hant/"), (["pt-PT"], "/pt-BR/"), (["in-ID"], "/id/"),
                            (["fr-CA"], "/fr/"), (["tr"], "/tr/")):
            self.assertEqual(self.detect(langs), want, langs)

    @unittest.skipUnless(shutil.which("node"), "node required")
    def test_unsupported_and_english_stay_on_the_root(self):
        for langs in (["ru-RU"], ["zh-CN"], ["ar-EG", "en"], ["hi-IN"], ["en-US"], ["xx-YY"]):
            self.assertIsNone(self.detect(langs), langs)

    @unittest.skipUnless(shutil.which("node"), "node required")
    def test_saved_choice_wins_and_survives_blocked_storage(self):
        self.assertEqual(self.detect(["en-US"], saved="ja"), "/ja/")
        self.assertIsNone(self.detect(["ko-KR"], saved="en"))
        self.assertEqual(self.detect(["ko-KR"], broken=True), "/ko/")

    @unittest.skipUnless(shutil.which("node"), "node required")
    def test_crawlers_and_pages_without_redirect_are_left_alone(self):
        self.assertIsNone(self.detect(["ko-KR"], ua="Mozilla/5.0 (compatible; Googlebot/2.1)"))
        self.assertIsNone(self.detect(["ko-KR"], redirect=False))
        self.assertIsNone(self.detect(["ja-JP"], options=[o for o in OPTIONS if o["lang"] != "ja"]))


if __name__ == "__main__":
    unittest.main()
