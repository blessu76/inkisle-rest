---
title: An ending that plays once, and a lighthouse to see it again
description: The season 1 ending of Inkisle plays by itself exactly once, the first time the last stage of act 30 is cleared. How we set the replay rules, how players who already cleared it and the act 10 ending are handled, and what we have not checked on translations or a real device.
slug: an-ending-that-plays-once
lang: en
category: making-of
keywords: Inkisle, season 1, ending, open ending, lighthouse, game design, mobile game
image_alt: A lone island on a calm sea with one lighthouse burning, and the chart route stopping in front of it.
published: 2026-11-22T16:00+09:00
---

The season 1 ending of Inkisle, our island-conquest strategy game for iOS, plays by itself once, the first time stage 8 of act 30 is cleared. To watch it again, the player taps the lighthouse at the top of act 30. The ending has no closing word; the only mark is "Inkisle · Season 1". This post is less about what the ending shows and more about when it plays and when it does not, and how we settled those rules. The game is in development and not released.

## Four rules

These are the replay rules we set when the ending went in.

- **Once, on the first clear.** It plays by itself the moment stage 8 of act 30 is first won.
- **Never again on its own.** Winning the same stage again, or restarting the app, does not play it automatically.
- **Skippable any time.** One tap goes to the final still frame, and a device with reduce-motion on starts at the still frame.
- **Replay is the lighthouse.** A lighthouse sits at the top of act 30, and tapping it plays the same ending again.

Even when an ending is under 30 seconds, we decided that "once, right after the win" is a gift and "every time you win" is an interruption.

## Where "already seen" is written

Whether it has played is kept as a story key in the save data. The key for the season ending is **deliberately separate** from the key for the act 10 ending. If both used one key, a player who had seen the act 10 ending could have the season ending counted as already seen. One test checks this: watching the act 10 ending leaves the season key untouched.

## Players who already cleared it

Someone may have cleared stage 8 of act 30 before the ending existed. For that save the first-clear moment has already passed, so nothing plays by itself and only the lighthouse appears. We chose not to force a moment that is gone, and to let the player press it when they want to.

In the same change, the act 10 lighthouse was moved to the top of act 10, where it belongs.

## What the tests pin down

The ending has 18 tests. The ones tied to these rules:

- It plays exactly once on the first win of stage 8 in act 30, and not when the player re-enters.
- Nothing plays at stage 7 of act 30 or at stage 8 of act 29.
- A save that already cleared stage 8 of act 30 gets no automatic playback, only the lighthouse.
- At 375px and 320px in widget tests, playing, skipping and leaving midway all work.
- The text of all 12 languages fits without overflow.

## No closing word

The last line, in Korean, is "The deep water reflects." (「깊은 물이 비친다.」). No language version carries a word like "The end", and the bottom mark is "Inkisle · Season 1". The replay rules come from the same thought: the story closes, but the app does not. After act 30 players can still replay acts, collect three stars and look at the score boards.

## What we have not checked

- **The ending text in the 10 languages other than Korean and English is machine-translated and has not been reviewed.** With only a few lines on screen, the quality of a translation shows immediately.
- The slow fade, the gold lettering and the bell volume have not been seen on a real device.
- 375px and 320px renders were checked only in widget tests, whose test font is much wider than the real one.
- Whether there will be a season 2 is undecided, and no release date is set.

## FAQ

### How many times does the ending play by itself?

Once, the first time stage 8 of act 30 is cleared. After that the player taps the lighthouse at the top of act 30 to see it again.

### Can the ending be skipped?

Yes. One tap jumps to the final still frame, and with reduce-motion on it starts at the still frame.

### Is the ending text reviewed in every language?

No. Translations other than Korean and English are machine-translated and not yet reviewed.
