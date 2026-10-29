---
title: Tuning difficulty with bots: five stages that were wrong
description: We played every stage with simple bots for 40 seeds each and found stages that were impossible, too short or too hard. The five changes, the win rates before and after, and why bots are not people.
slug: tuning-the-difficulty
lang: en
category: making-of
keywords: Inkisle, game balance, difficulty tuning, bot simulation, win rate, level design
image_alt: A crowded battle between several colored sides on the Inkisle prototype.
---
We have no playtesters yet, so we asked a different question: which stages are *obviously* wrong? Two simple bots played every stage 40 times each, with 40 different seeds, and we read the win rates.

## The two bots

- **Simple bot:** every 10 ticks it attacks the cheapest island it can beat. It stands in for a casual player.
- **Skilled bot:** every 5 ticks it gathers up to three islands and attacks together.

Neither is a person. They tell us direction, not difficulty as a human feels it.

## Five stages that were wrong

| Stage | Problem | Change | Simple bot before → after |
|---|---|---|---|
| 1-1 | Three-star goal "lose at most 5" was impossible: the neutral islands alone cost 13 | Goal changed to "at most 14" | Three stars reached 0% → 100% |
| 1-5 | Over in 18 seconds | Enemy home 20 → 26, one neutral island given to the enemy | 100%, now 30 s |
| 1-8 boss | Practically unbeatable | Enemy's second island made smaller, flag island 24 → 26, one small island handed to the player | **0% → 53%** |
| 2-2 | Over in 23 seconds | Player home 15 → 20, one island given to the enemy | 100%, now 38 s |
| 2-8 boss | Too hard | Flag island 24 → 28, one enemy fortress made a neutral fortress of 14 | **10% → 38%** |

We left the other 11 stages as they were. The target was a boss stage that a casual player beats after about one retry, so 40 to 60% for the simple bot.

## Side effects we noticed

- Across a 20-seed set, the simple bot's overall win rate went from 84% to 91% and the skilled bot's from 78% to 82%.
- Stage 2-2 got *harder* for the skilled bot, 100% down to 65%. We think the bot has a habit of emptying fortresses, but that is **[unverified]**.
- Stages 2-4 and 2-7 show low win rates for the skilled bot, 40% and 38%. In a crowded fight, gathering may hurt. Also **[unverified]**.
- The two-star time limits look too generous, since bots meet them nearly always. We will tighten them after we see human times.

![Three phone screens from busy battles in the prototype. The text in the screenshots is Korean.](/assets/posts/img/tuning-boss.jpg)
*Busy stages in the prototype: a mid-sea melee, a boss stage with the flag island ringed, and a 320 px-wide screen.*

## Why bots are not people

A bot never misreads a number, never gets bored and never mis-drags. A person's first 30 minutes are the real test: where they retry, where they quit, how long they take to reach "next". The plan is to add a play log first and then watch five to eight people. Until then these numbers say only that no stage is clearly broken, and that is a weaker claim than "the difficulty is right".
