---
title: The rules on one page: islands, troops, capture
description: Inkisle's whole rule set on one page: how islands produce troops, how fleets fly, how capture is calculated, and how a match ends. Starting values, before testing.
slug: the-rules-on-one-page
lang: en
category: making-of
keywords: Inkisle, game rules, island conquest, deterministic engine, game design, capture rules
image_alt: Islands with troop numbers and dotted routes where fleets travel between them.
published: 2026-10-30T05:40+09:00
---
Good strategy games can be explained in a minute. This is our attempt at Inkisle's rules, on one page. **Every number here is a starting value from the design document.** We expect to change some of them after testing, and the posts later in this series show which ones already changed.

## Islands make troops

- Each island you own adds **1 troop per second** (a "tick" is 100 ms, so one troop every 10 ticks).
- There is a **cap** of 45. Past the cap an island stops producing, and extra troops from reinforcements drain back to the cap at 1 per second. That stops you from piling everything on one island and waiting.
- **Neutral islands do not produce.** Their number is fixed, so it reads like a price tag.
- You start with a home island of 20 troops. The enemy usually does too, and if not, the stage card says so.

## Sending fleets

Drag from one of your islands to another island and let go. A bar at the bottom picks the share: **25, 50, 75 or 100%**. You send the floor of troops times the share, at least 1. At 100% you send "all minus one", so the island never becomes empty and stays yours.

A fleet flies in a straight line at **2.5 map units per second**. A neighboring island 4 to 8 units away takes about 1.6 to 3.2 seconds, and crossing the whole map takes about 11 seconds. Fleets do not fight on the sea; they pass each other. That keeps the arrival preview honest, and the genre's tension remains: a long trip is a risk, because the target keeps growing while you travel.

## Capture, calculated at arrival

- Arriving at your own island adds the troops.
- Arriving at an enemy or neutral island, you need more than **defense times the multiplier**. The multiplier is 1.0 normally and **1.5 for a fortress**.
- Attack above the requirement: you capture, and the new defense is the leftover. Equal: the defender holds with 0 (ties go to the defender). Below: the defender loses a share.

Two examples. A fleet of 18 arrives at a fortress of 10. The requirement is ceil(10 × 1.5) = 15, so you capture it with 3 left. A fleet of 12 arriving at the same fortress leaves it with 2.

If several fleets arrive in the same tick, they resolve one by one in the order they left.

## How a match ends

- **Win:** the enemy has no islands and no fleets.
- **Decisive win:** if you hold three times the enemy's total troops and at least 60% of the islands for 5 seconds, the enemy gives up. This ends the boring mop-up of an already won match.
- **Loss:** you have no islands and no fleets, or you lose an island you were told to protect.
- **Time limit:** at 8 simulated minutes the player with the most islands wins. This should almost never trigger.

## One engine for real time and turns

The game state depends only on the starting map, a seed and a list of commands, with no clock and no randomness inside the engine. The same input gives the same result on every device. That is what lets the same engine run in real time now and in networked turns later, and it makes replays and bug reports a matter of saving a command list.
