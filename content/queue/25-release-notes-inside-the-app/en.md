---
title: Release notes inside the app: a 12-language sheet and a length check
description: Inkisle's release notes are a sheet inside Settings, not a web page. How each build's notes are written in 12 languages, the checks on item count and length, and the test bug that showed an empty sheet.
slug: release-notes-inside-the-app
lang: en
category: making-of
keywords: Inkisle, release notes, localization, multilingual, testing, mobile game
image_alt: One sheet of paper rising from the bottom of a screen, with twelve small language tabs in a row above it.
---

The release notes of Inkisle, our island-conquest strategy game for iOS, are an in-app sheet opened from Settings, not a web page. Each build's notes are written in 12 languages, and a check script verifies the item count and length. The check for build 34 reported 0 errors and 0 warnings. The game is still in development and not released.

## We removed the web page

At first the main screen had a "Release Notes" link and an info button (ⓘ). In build 32 we removed both. What the info window held (privacy policy, terms, version, open-source licenses, operator, contact and the 16+ notice) moved into Settings, and release notes became a sheet opened from a "Release notes" row there. The release-notes page on the website was also taken out on November 15. With no separate site, the text inside the app is the only source.

The sheet uses the same frame as our other popups (InkSheet). It is at most 60% of the screen height, the title row and the close X (48×48) stay fixed, and only the body scrolls inside.

## One build, one file, 12 languages

For each build, `release_notes/<build>.json` holds a title, an intro and items in 12 languages (ko, en, ja, zh-Hant, es, pt-BR, fr, de, id, th, vi, tr). The files are bundled into `assets/release_notes.json`, which ships in the app, and the sheet reads that.

## Checks on length and count

A check script reads the files and reports rule breaks.

- **RN06:** an item must be 200 characters or fewer. The German text ran long, so the season-ending item in build 34 was cut to 183 characters. In build 31 we split one purchase item in two to fit the limit.
- **RN05:** 3 to 6 items are recommended. It is only a warning and does not block a release. The remaining warnings are on old builds with 1 or 2 items; they are an honest record of what was written, so we left them.
- A test fails if there is no entry for the current version and build number, so every build bump needs the 12-language note written first.
- The iOS upload script runs the release-notes check before the green gate (format, analyze, tests).

## The test that saw an empty sheet

Two release-notes sheet tests began to see an empty sheet. The cause was the test, not the app. The bundle is a real asset file, and as it grew, `pumpAndSettle`, which waits for the screen to settle, finished before the file read did. We changed the tests to open the sheet, wait 300 ms with `runAsync`, and draw again. The app code did not change.

## What we have not checked

- Translations other than Korean and English are machine-made and have not had a native-speaker review [unverified].
- We have not seen the sheet open at 60% on a real device. Widget tests at 375×667 and 320×568 stand in for it [unverified].

## FAQ

### Where do I find Inkisle's release notes?

In the app, tap the "Release notes" row in Settings and a sheet opens. There is no separate web page. The game is not released yet.

### How many languages are they written in?

12 languages. Apart from Korean and English they are machine-translated and not yet reviewed.

### What happens if an item is too long?

If one item goes over 200 characters, the check script reports an error, so we shorten it or split it in two.
