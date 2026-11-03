---
title: Two Ink items at once: slots, gaps and what the bots told us
description: In early seas you could run one Ink item at a time. From sea 5 you can run two, and later three, with a gap between starts. The rule table, how the button shows it, and a simulation that found a much smaller effect than we expected.
slug: two-inks-at-once
lang: en
category: making-of
keywords: Inkisle, Ink items, game design, game balance, bot simulation, mobile UI, accessibility
image_alt: Two small ink drops side by side above a row of islands, drawn in soft vector colors.
---
Ink items (surge, anchor, mist, lantern, tide flip) used to run one at a time. That is easy to understand and it also means a later stage can never feel like you have more tools. So we gave the Ink button **slots**.

## The rule

| Sea | Slots at once | Gap between starts |
|---|---|---|
| 1 to 4 | 1 | none (as before) |
| 5 to 10 | 2 | 10 seconds |
| Volume 2, seas 11 to 20 | 2 | 5 seconds |
| Volume 3, from sea 21 | 3 | 5 seconds |

What stayed the same: a boss adds 5 seconds to the gap, the per-stage cap on uses (5 or 6) is shared by all slots, you cannot run two of the same kind, an anchor or mist slot is freed when its island is captured, and the first 20 seconds of a stage still lock every Ink.

## How the button shows it

The Ink button has one dot per slot, filled while a slot is running. A thin ring inside the button counts the gap before you may start the next one. In the harbor sheet, a blocked card says "next Ink in N seconds" for the gap or "spreading" when the slots are full. The accessibility label reads like "1 of 2 slots". All of this is in 12 languages.

## Why the engine did not need a new hash

The game state already holds a list of end times for running Ink and the count of uses, so seas 1 to 4 behave and hash exactly as before. Tests cover each row of the table, the first-sea behavior, same-kind refusal, full slots, three slots, the shared cap and the release on capture, plus the button at 320 and 375 px.

## What the bots said

We simulated 80 stages from sea 5 to 14, five bots, 24 seeds each, for four plans of two or three items starting at 20 seconds, and compared the best plan under the old rule (one slot, no gap) with the new rule.

- The average gain was **+1.1 percentage points** (+0.9 in seas 5 to 10, +1.5 in seas 11 to 14). We had expected 3 to 8.
- In bosses it was +0.9. The best Ink win rate over no Ink was +36 points, inside our limit of 40.
- Stage by stage the change moved between −7 and +10, which is about the noise of 24 seeds.

The bots rarely use the second slot well, so the small number may say more about the bots than about the rule. **[unverified]** A person could gain more.

## What we have not checked

- Whether a person finds two slots and a gap clear, or whether it feels like a lock. We have not tested it on a real phone. **[unverified]**
- A one-line notice the first time a player reaches a two-slot sea (5-1) is not built yet.
- The game is in development and is not released.
