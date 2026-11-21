---
title: Skip a stage after three losses: a gentle offer with a cost
description: In Inkisle, losing the same stage three times offers to skip it for 3 Ink. How the offer is timed, which stages are excluded, how a skipped stage shows on the chart, and how it is saved.
slug: skip-a-stage-after-three-losses
lang: en
category: making-of
keywords: Inkisle, skip stage, difficulty, game design, save data, mobile game
image_alt: A sea chart with one island marked by a small coral flag, and a dotted path leading past it to the next island.
published: 2026-11-21T12:30+09:00
---

In Inkisle, our island-conquest strategy game for iOS, losing the same stage three times brings up a question: "Skip this stage and try it later?" Skipping costs 3 Ink. The skipped stage gets a flag on the chart and can be played whenever you like. The game is still in development and not released, and we have not yet seen this popup on a real device.

## Why offer a skip at all

Some stages stay hard even after the difficulty tuning. We did not want a player to stop at one island. The offer lets them move on and come back, instead of quitting the game.

## When it asks

- The popup appears after the **third loss** of the same stage, once the result sheet has settled (1.1 seconds).
- If the player says no, it does not ask after the 4th and 5th loss. It asks again at the **6th, 9th** and so on. Asking every time would be nagging; asking only once would miss a player who is still stuck.
- Losses are counted per stage. Winning the stage resets the count to 0. Losses on a stage that is already cleared or skipped are not counted.

## What it costs

A skip costs **3 Ink**, the same Ink the player already earns in the game or buys. No new currency and no new product was added. The value is one constant in the code, and the popup text, the button and the link to the shop all follow it.

We first set it to 1 Ink, then raised it to 3 after the owner asked for 2 to 3. If the player has fewer than 3 Ink, the skip button becomes "No Ink, open the shop" and opens the existing shop sheet. With 3 or more, the skip button comes back.

## Which stages are excluded

- Stages 1-1 to 1-4, the tutorial stretch without Ink. Skipping there would mean never learning the controls.
- Stage 1-5, where the game gives its first Ink as a gift.
- The last stage, because there is no next stage to open.
- Boss stages are included.

## What a skipped stage means

- The next stage opens, and the skipped stage has **0 stars**. A skip is not a clear, so stars cannot be bought.
- On the chart, the node gets a coral flag. Screen readers add "skipped". The stage card says "This stage was skipped. Challenge it again whenever you are ready."
- Beating it later removes the flag and records the stars normally.
- A sea is complete only when its stages are cleared, so a flagged stage still has to be won to complete the sea.
- The ending opens only on a real win, so skipping stage 10-8 does not open it.

## How it is saved

The existing progress record gets two optional keys: the failure count per stage and the list of skipped stages. If both are empty, the keys are not written, so an old save stays byte for byte the same. On reading, unknown ids and negative or text values are dropped, and a stage that is already cleared loses its skip mark, because the clear wins.

For iCloud merging, the larger failure count is kept, skipped lists are joined, and a clear on another device wins. Merging the same snapshot again changes nothing, and a test checks it.

## What we have not checked

- The popup and flag on a real device or simulator. Widget tests at 375 and 320 px width found no overflow in 16 language columns, but we did not look at screenshots.
- Whether an older app version that overwrites the iCloud snapshot drops the two new keys. If so, cleared stages and stars stay, and we expect only the skip marks to be lost.
- Translations other than Korean and English have no native-speaker review.

## FAQ

### When does Inkisle offer to skip a stage?

After you lose the same stage three times, and again after the 6th, 9th loss and so on if you keep going. The first stages, the 1-5 gift stage and the last stage are excluded.

### What does a skip cost, and do I get stars?

It costs 3 Ink. A skipped stage gives 0 stars. If you beat it later, you get the stars as usual.

### Does skipping finish a sea or open the ending?

No. A sea counts as complete only when its stages are cleared, and the ending opens only on a real win.
