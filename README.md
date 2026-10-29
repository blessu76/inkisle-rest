# inkisle.ipe.rest

Home page and production journal of **Inkisle** (F-019), an island-conquest strategy game by ipe() — *in development, not released*.
Static site on GitHub Pages (`CNAME` = inkisle.ipe.rest). Python 3.8+ standard library only; no build dependencies.

| Path | Role |
|---|---|
| `content/i18n/<lang>.json` | UI strings + home copy, 12 languages (`en` root, `ko` original, 10 AI translations) |
| `content/pages/<lang>/{about,privacy}.md` | about / privacy policy |
| `content/journal/<slug>/<lang>.md` | **published** posts. Front matter incl. `published: YYYY-MM-DDTHH:MM+09:00` |
| `content/queue/NN-<slug>/<lang>.md` | queued posts (no `published:` yet). `NN-` orders the queue |
| `scripts/build_site.py` | generator → `index.html`, `<lang>/…`, `journal/…`, `sitemap.xml`, `robots.txt`, `llms.txt`, `*/feed.xml`, `404.html` (generated, never hand-edit) |
| `scripts/publish_post.py` | queue → journal (stamps the time, refuses future), then build + sitemap check |
| `scripts/check_sitemap.py` | sitemap ↔ files ↔ posts ↔ hreflang consistency (`--live` after deploy) |
| `scripts/indexnow.py` | IndexNow ping (key file `<32 hex>.txt` at the root) |
| `scripts/make_art.py`, `render_png.js` | vector art (logo, hero, covers) and the PNGs (og image, icons) |
| `scripts/check.sh` | **green gate** — run before every commit |
| `docs/TRANSLATION.md` | translation pipeline |
| `ops/` | daily 19:00 KST publish: script + launchd plist (installed by the room lead, not by the repo) |

## Everyday commands

```
python3 scripts/build_site.py             # rebuild generated files
bash scripts/check.sh                     # sources, tests, "build is up to date", sitemap — must print GREEN
python3 scripts/publish_post.py --dry-run # what the next publish would do
python3 scripts/publish_post.py           # publish the head of the queue now (then commit + push)
python3 scripts/check_sitemap.py --live   # after deploy: every URL is HTTP 200
python3 scripts/indexnow.py <URL> ...     # after deploy: tell Bing/Naver/Yandex
```

URLs: English at the root (`/`, `/about/`, `/privacy/`, `/journal/`, `/journal/<slug>/`), every other language under `/<lang>/…` with the same slugs;
`hreflang` links all language versions and `x-default` = English.

## Rules this site follows (company policy: REACH_PROCESS, ADR 0085)

- One journal post a day while the app is unreleased; the recorded time is the real publish time, never in the future.
- Honest status: Inkisle is *not released*; no store link, date or price is promised anywhere. Unchecked things are marked **[unverified]**.
- SEO/GEO: hreflang (12 + x-default), JSON-LD (WebSite, VideoGame, Blog, BlogPosting, BreadcrumbList), sitemap, robots (AI crawlers allowed), llms.txt, RSS, IndexNow.
- No secrets, local paths or internal tool names in public text (the build refuses them).
- After changing `assets/inkisle.css` or `inkisle.js`, bump `ASSET_V` in `scripts/build_site.py` (cache busting `?v=`) and rebuild.
- Before deploying UI changes: check 375 / 320 / 768 / 1280 px for horizontal overflow (see `tests/ui_check.js`).
