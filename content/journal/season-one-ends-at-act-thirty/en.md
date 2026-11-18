---
title: From 100 acts to 30, and an ending that stays open: the end of season 1
description: The first plan was 100 acts and 800 stages. Why we closed season 1 at 30 acts and 240 stages, how we kept the 100-act plan as a candidate instead of dropping it, and how the ending with no closing word was made.
slug: season-one-ends-at-act-thirty
lang: en
category: making-of
keywords: Inkisle, season 1, 30 acts, ending, open ending, game design, mobile game
image_alt: A long sea route on a chart that stops before a calm sea, with one small light burning on the last island.
published: 2026-11-18T19:02+09:00
---

Season 1 of Inkisle, our island-conquest strategy game for iOS, ends at act 30 with 8 stages per act, 240 stages in all. The first plan was 100 acts and 800 stages; we kept that plan as a candidate for a season 2 instead of dropping it. The ending of act 30 is three scenes in under 30 seconds and it never says "the end". The game is still in development and not released.

## Why we cut it down

The first goal was 100 acts × 8 stages = 800 stages. That is why some earlier posts, on the difficulty curve and the chart route, are written with 800 stages in mind. On November 15 the owner changed the decision: **season 1 ends at act 30, with an ending shown after act 30.**

The decision record gives no long reason. What it does record is that 23 acts were finished at that point and 77 were left, and that the decision made acts 27 to 30 plus an ending the remaining work for season 1. Why exactly 30 is [unverified]; the structure the documents give is that three volumes of ten acts make one story that can close.

## The 100-act plan is not thrown away

Volumes 4 and up (acts 31 to 100) are kept in the documents as "season 2 candidate". Volumes 1 to 3 are the same as season 1, so only volume 4 onward is candidate material. **Nothing has been decided about making a season 2.** If we do, we would first recount the acts and decide how to connect it to the act 30 ending.

## Three volumes

| Volume | Acts | Theme |
|---|---|---|
| 1 | 1 to 10 | The basic rules of spreading ink |
| 2 | 11 to 20 | Roads and flow (chart lines, tides) |
| 3 | 21 to 30 | Two inks meet, erased lines and joining hands |

Act 26 is the story's peak, and acts 27 to 30 come down from it and converge. The act 30 boss uses a new win condition: hold more than half the islands for 30 seconds together with an allied fleet (not by taking every island). The bot win-rate target for it was 32%.

## The ending: no closing word

We made two decisions. One is an **open ending**. The last line is a translation of the Korean "The deep water reflects.", and there is no "The end" in any language. The other is that the ending screen says "Inkisle · Season 1". Store text speaks only of "30 acts".

- **Scene 1:** four lines of text rise slowly over spreading ink.
- **Scene 2:** a night veil comes down and the journey appears in gold lettering: seas crossed, stages won and stars collected, counting up from 0. The numbers are computed from the saved record.
- **Scene 3:** the calm sea returns with the last line, "Inkisle · Season 1" and one line of thanks.

The whole thing runs under 30 seconds, and one tap skips to the final still frame. A bell rings exactly once in scene 3, and not at all if the player skipped, has reduce-motion on, or has sound effects off. The ending plays by itself once, the first time act 30 stage 8 is cleared. To see it again, the player taps the lighthouse at the top of act 30.

## Fixing the word "last"

If the season ends at act 30, earlier words like "last" no longer fit. We found three lines in acts 10 and 11 ("the last sea", "the end of the map") and changed them to open wording, for example "Beyond it, the map has nothing yet."

## What we have not checked

- The slow fade, the gold look and the bell volume have **not been seen on a real device [unverified].** So far we checked 375px and 320px renders only in widget tests.
- Ending text in languages other than Korean and English is machine-translated and not reviewed [unverified].
- There is no season 2 plan, and no release date has been set.

## FAQ

### How many stages are in Inkisle season 1?

30 acts with 8 stages each, 240 stages in all. The game is still in development and not released.

### Did you drop the 100-act, 800-stage plan?

No. Volume 4 onward is kept as a season 2 candidate, and we have not decided to make a season 2.

### Does the game end when the ending plays?

No. Replaying acts 1 to 30, collecting three stars and the score boards continue. The ending closes the story, not the app.
