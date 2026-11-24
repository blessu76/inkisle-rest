---
title: What we guard when upgrading a shared kit: a 2,561-test gate
description: Every time Inkisle upgrades the shared kit our apps use, it must pass a format, analysis and full-test gate. Why we did not replace a whole kit feature, how timing tests wobbled under load, which files changed in the latest upgrade, and what we have not checked.
slug: a-shared-kit-and-2561-tests
lang: en
category: making-of
keywords: Inkisle, shared kit, tests, Game Center, upgrade, mobile game
image_alt: Several small blocks of the same shape sitting in one frame, with a single green dot passing across them.
published: 2026-11-24T12:45+09:00
---

Inkisle, our island-conquest strategy game for iOS, uses a shared kit that several of our apps rely on. Each time we raise the kit's version, one gate runs format, static analysis and the full test suite before we commit. On November 19 we moved the kit from 0.15.2 to 0.15.3: the gate passed 2,561 tests (8 skipped), and only two files changed, `pubspec.yaml` and `pubspec.lock`. This post is about how that number is kept and what wobbled along the way. The game is in development and not released.

## The gate has three steps

One script runs them in order before a commit: code formatting must not change, static analysis must report 0 issues, and all tests must pass. If any fails, we do not commit. When someone else says "it passed", we run it again ourselves before committing.

## November 14: we did not replace the whole kit feature

Moving the kit from 0.12.0 to 0.13.0 let it handle the nickname and the Game Center leaderboard. The owner's instruction was that every game should let the player set a nickname on first launch and appear on the Game Center leaderboard. We did **not swap in the kit's whole player feature.** We had four reasons to think our own version was better:

1. The nickname lives inside the settings record, which syncs across devices through iCloud. Moving it to the kit's storage would break that sync.
2. We already have a nickname sheet in 16 languages and tests frozen across language and screen-size combinations.
3. The leaderboards are 24 dynamic boards, with values derived from the synced progress record. Moving them would leave two places that store a best score.
4. Android's Play Games still needs the library it uses.

So only the iOS Game Center connection moved to the kit, and the board IDs, saved nicknames and best scores carried over unchanged. Re-sending a backlog after a late sign-in and prefilling the nickname with the Game Center name went in at the same time. We added 10 tests, and the gate then passed 1,990 tests (7 skipped).

## Timing tests wobbled

Twice in this gate, a test that measures time wobbled under load. A frame-budget test that draws 800 roads failed once when tests ran in parallel, and during the iCloud work a performance-budget test failed once. Both passed when run alone or when the full suite was run again. We read this as load, not our change, though we did not trace the cause. We did not loosen the budgets.

## November 19: two files changed

Version 0.15.3 leaves the public API as it was; it makes a re-count in the iCloud sync stop after teardown and adds documentation. We changed no code and no tests in the app. The size limit the app uses (512 KB) is intended, so we kept it. The changed files were `pubspec.yaml` and `pubspec.lock`, and the gate passed on its first run, with no timing wobble this time. The test count grew from 1,990 on November 14 to 2,561.

## What we have not checked

- **Game Center sign-in, score submission, the leaderboard screen and an iCloud round trip have not been checked on a real device.** We will look in TestFlight.
- 375px and 320px renders were covered by widget tests at 320×568 rather than seen directly.
- We did not find the root cause of the tests that wobbled under load.
- The numbers here are that day's gate results, and the test count will change later.

## FAQ

### What is the shared kit?

A bundle of code that several of our apps use together. Inkisle uses its nickname, Game Center and iCloud sync parts.

### What do you check when upgrading the kit?

One script checks that formatting does not change, that static analysis reports 0 issues and that all tests pass. If any fails, we do not commit.

### Is the game released?

No. It is still in development and not released.
