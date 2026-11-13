---
title: The white sea's ink spring: when a three-star rule cannot be earned
description: Sea 14 has a spring that spreads ink onto nearby islands. Bots could not earn the three-star goal "make the spring spread to N islands", so we measured, tried moving islands, and replaced the rule with a count of spring pulses. What we tried and what is still unchecked.
slug: the-white-sea-ink-spring
lang: en
category: making-of
keywords: Inkisle, level design, three-star rule, ink spring, bot simulation, game balance, sea 14
image_alt: A pale sea with a small spring island at the center and a few islands around it, drawn in soft vector colors.
published: 2026-11-10T19:00+09:00
---
Sea 14, the white sea, adds one rule: an **ink spring**. Hold the spring island and, every 150 ticks, it pulses and spreads ink onto a nearby island. The first pulse comes 150 ticks after you capture it. The three-star goal we first wrote for it was "make the spring spread to N islands". That goal turned out to be a promise nobody could keep.

## The measurement

The goal was used in seven stages. In six of them we scripted the best play we could think of: capture the spring at tick 0, then leave it alone for 900 ticks, with four seeds each. (14-8 cannot be scripted this way, because the enemy holds the spring from the start.)

| Stage | Spreads needed | Spreads we got |
|---|---|---|
| 14-1 | 2 | 0 |
| 14-2 | 2 | 0 |
| 14-3 | 3 | 0 |
| 14-5 | 2 | 0 |
| 14-6 | 2 | 0 |
| 14-7 | 3 | 0 |

The enemy takes the small islands beside the spring between tick 70 and tick 250. The first pulse arrives at tick 150 or later, so there is often nothing left to spread to.

## Three things we tried

1. **Move the islands.** A search over small islands beside the spring found layouts that reach the needed number in 14-1 and 14-5, but only by putting four or five small islands beside the spring. That breaks our own cap of three, and 14-5 then fails the "the simplest bot must win at least a few times" floor. Inside the cap, no layout gave more than one spread.
2. **Make the first pulse earlier.** With the first pulse at 60 ticks, 14-1 becomes possible and the other five stages stay at 0 or 1. It also pushed 14-8 below our floor for the simplest bot. We did not keep it.
3. **Change the rule.** The goal should reward what the player controls: holding the spring. So the three-star goal became the **number of pulses of your own spring**. The numbers, picked at or below what bots actually reached in won games: 14-1: 4, 14-2: 3, 14-3: 2, 14-5: 3, 14-6: 1, 14-7: 3, 14-8: 1. Stage 14-4 keeps its separate goal.

We chose the third. It touches only sea 14, so the hashes and golden files of seas 1 to 13 did not change.

## A last pass on the sea

Alongside, we widened the middle of 14-1 (a central island from 4 to 12) and eased 14-6, where one bot won far more than the others. A new test now says that no single bot may take more than half of the wins in 14-8; today it is 8, 17, 12 and 24 wins for four bots and 0 for the fifth.

## What we have not checked

- In 14-6 and 14-8 the enemy holds the spring, so one pulse is the most you can count on. Bots rarely reached it, so the numbers rest on thin data. **[unverified]**
- Nobody has played these stages by hand. Whether "make the spring pulse" feels clear on the stage card and the result screen needs a real phone. **[unverified]**
- The game is in development and is not released.

## FAQ

### What is the ink spring in sea 14 of Inkisle?

A spring island you hold pulses every 150 ticks and spreads ink onto a nearby island. The first pulse comes 150 ticks after you capture it.

### Why was the three-star goal changed?

The first goal, make the spring spread to N islands, was never reached: our scripted best play got 0 spreads in all six stages tested.

### What is the goal now?

The number of pulses of your own spring, such as 4 in stage 14-1. It touches only sea 14, so seas 1 to 13 did not change.
