---
title: A difficulty curve with a floor: no stage the simplest bot can never win
description: With hundreds of stages, a few hard ones are not a few hard ones, they are a wall. We retuned all 14 seas to a curve with a rest stage in every sea, capped how strong the enemy AI may be, and added a test that fails if the simplest bot wins 0 of 40. The before and after.
slug: a-difficulty-curve-with-a-floor
lang: en
category: making-of
keywords: Inkisle, difficulty curve, game balance, bot simulation, level design, win rate, AI level
image_alt: A winding row of islands that rises and falls like a wave, drawn in soft vector colors.
published: 2026-11-11T19:00+09:00
---
A comment from the owner changed this work: if only 40 of 800 stages are winnable, the game is too hard, even if each stage looks fine alone. So we stopped tuning stages one by one and wrote down a **curve**.

## The curve

- Each sea has eight stages with a **role**: opener, build-up, a rest stage, climb, boss. The rest stage is meant to be easy, with the simplest bot winning at least 80% of the time.
- The target win rate also follows a **wave across the volumes**: a sea is a little harder than the one before it, then there is a gentler sea again.
- Seas 1 to 3 are already in TestFlight builds, so we left their easy values alone.

## A cap on the enemy

Some stages were hard because the enemy AI was too clever, not because the map was tough. We added an **AI ceiling**: level 5 only for stages with several enemies, level 4 for seas 11 and up and for bosses and the seventh stage from sea 6, level 3 everywhere else. Any AI above its ceiling is lowered when the stage loads. One example: in 10-8 the admiral went from level 5 to 3, and the neutral lighthouse's defence from 10 to 5.

## The measurement

All 14 seas, five bots, 40 seeds each. "Simple bot" is the weakest of the five and stands in for a person.

| | Before | After |
|---|---|---|
| Stages the simple bot never wins | **9** (3-8, 4-3, 4-6, 5-5, 6-8, 7-6, 10-3, 10-8, 14-2) | **0** |
| Weakest stage | 0 wins of 40 | 4 wins of 40 (8-8), then 5 of 40 (10-8) |
| Rest stages, simple bot | not tracked | at least 80% |

Some examples of the simple bot's wins out of 40: 3-8: 0 → 30. 4-3: 0 → 18. 6-1: 2 → 39. 7-6: 0 → 17.

## A test that holds the floor

`curve_floor_test` fails if the simple bot wins 0 of 40 anywhere, if a rest stage falls below 80%, or if the average of the five bots drifts too far from the curve target. The targets live in one file, so changing the curve is changing one table.

## What got easier on purpose, and the cost

Making stages easier made the **Ink** items worth more, because a stage that is easier to win also gains more from a bonus. To keep the stages we wanted, we loosened two Ink guards: the cap on a boss's win rate with Ink went from 55% to 75% in five boss stages, and the gain from one use of Ink went from 25 to 35 percentage points in four stages. These are exceptions we wrote down, and they still need a decision on how much Ink should be worth. **[unverified as a policy]**

## What we have not checked

- Win rates are from bots. A few stages (4-6, 5-7, 9-5, 10-2, 10-3, 11-6) sit about ten points off the target, and 10-8 has a bot average of 62% against a target of 33%, because the admiral is very hard for the simplest bot but easy for the others.
- Nobody has played the new curve by hand, so "40 of 800 is too hard" is fixed only in the bots' numbers. **[unverified]**
- The game is in development and is not released.

## FAQ

### What is the difficulty floor in Inkisle?

A test fails if the simplest bot wins 0 of 40 games on any stage. After the retune, the weakest stage was 4 wins of 40.

### What does the enemy AI ceiling do?

It caps enemy AI at level 5 for multi-enemy stages, level 4 for seas 11 and up and some bosses, and level 3 elsewhere.

### Is the curve proven for human players?

No. The numbers come from bots, and nobody has played the new curve by hand.
