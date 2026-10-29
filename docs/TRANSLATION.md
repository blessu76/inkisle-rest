# Translation pipeline (12 languages)

`en` and `ko` are written by hand (originals). The other ten — `ja zh es fr de pt ru ar hi id` — are **AI translations of the English original**
(`translation_of: en`), shown on the site with an "AI translated" notice that links to the original.

## What gets translated

| Source (English original) | Target | Notes |
|---|---|---|
| `content/i18n/en.json` | `content/i18n/<lang>.json` | same keys, translated values. Keep `Inkisle`, `InkIsle`, `ipe()` untouched |
| `content/pages/en/about.md`, `privacy.md` | `content/pages/<lang>/about.md`, `privacy.md` | add `translation_of: en` to the front matter; keep `{{EMAIL}}` `{{OPERATOR}}` `{{EFFECTIVE}}` placeholders; internal links get the language prefix: `/journal/` → `/<lang>/journal/`, `/privacy/` → `/<lang>/privacy/` |
| `content/journal/<slug>/en.md` or `content/queue/NN-<slug>/en.md` | same folder, `<lang>.md` | front matter: `lang: <lang>`, add `translation_of: en`; translate `title`, `description`, `keywords`, `image_alt`; keep `slug`, `category` and (if present) `published` exactly as in the original |

## Rules for the translator

1. Meaning first, natural phrasing in the target language. Not word by word.
2. Keep every number, unit, date, URL, file path (`/assets/posts/img/...`) and Markdown structure (headings, tables, lists, image + caption line) identical.
3. Keep brand names as they are: Inkisle, InkIsle, ipe(), GPT, iOS, Android, Grace, App Store, Google Play.
4. The honesty markers `[unverified]` / `**[unverified]**` must stay visible in the translation, in the target language (e.g. 【未検証】 for ja), still bold where the original is bold.
5. Do not add or remove claims. Do not invent a release date, price or platform commitment: the game is **in development and not released**.
6. No secrets, local paths or internal tool names. (The build refuses `/Users/`, `claude.ai/` and similar.)
7. Arabic (`ar`) is right-to-left: translate normally; the site sets `dir="rtl"`. Keep Latin brand names and numbers as they are.
8. UTF-8, no BOM. `content/i18n/<lang>.json` must stay valid JSON with exactly the keys of `en.json` (the build lists missing or extra keys).

## Check

```
python3 scripts/build_site.py --check              # sources valid for the languages that exist
python3 scripts/build_site.py --require-all        # every post in every one of the 12 languages
python3 -m unittest discover -s tests
```

## Daily flow

A post may be published before its translations exist: `publish_post.py` warns and publishes the languages it has. Add the missing
`<lang>.md` files later in `content/journal/<slug>/` (keep the same `published:` line) and rebuild — the new language pages and their
hreflang links appear automatically.
