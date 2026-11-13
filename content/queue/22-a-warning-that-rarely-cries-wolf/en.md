---
title: Bots as playtesters: a warning that rarely cries wolf
description: A crisis warning should only appear when you are really about to lose. We replayed thousands of bot games to measure false alarms, and the same run showed a star goal almost nobody wins.
slug: a-warning-that-rarely-cries-wolf
lang: en
category: making-of
keywords: Inkisle, playtest, bot simulation, game balance, warnings, mobile game
image_alt: A small bell above an island map with one island flashing in a soft warning color.
---

Inkisle, our island-conquest strategy game for iOS, warns you when a stage looks lost, and in a bot simulation of 3,360 games the warning was a false alarm only 3 times out of 2,096 wins (0.14%). When it showed, the bot lost 98.9% of the time. The same run showed that the star goal of stage 2-5 is almost never reached. The game is still in development and not released.

Inkisle can warn you when a stage looks lost. A warning is only useful if it is almost always right: if it shows up in games you go on to win, you stop trusting it. We had no outside players yet, so we asked bots to play.

## The test

Five bot styles, 112 stages, six seeds each: 3,360 games, plus 672 games where nothing is done. The warning is checked the way the game checks it, and the first time it fires counts. Bots do not use Ink in a crisis.

| | Games |
|---|---|
| Warned, then won (false alarm) | 3 |
| Warned, then lost (true alarm) | 262 |
| Not warned, lost (missed) | 1,002 |
| Not warned, won | 2,093 |

## What it says

### False alarms and misses

- **False alarms: 3 of 2,096 wins, 0.14%.** Our limit was 10%. The three were a boss each: 2-8, 8-8 and 13-8.
- When the warning showed, the bot lost 98.9% of the time.
- It warns in only 20.7% of the games that were lost. That is on purpose: it speaks only when sure, so most losses come without a warning.
- An old note said that in 16 do-nothing games, 8 got a warning, which looked like many false alarms. But a game where you do nothing always ends in a loss, so those were true alarms. In the new run, 115 of 672 do-nothing games warned (17%), and all of them were losses.

## Same run, another finding

### A star goal almost nobody wins

The star goal in stage 2-5, losing at most 60 troops, is almost never reached. One bot style got it in 3 of 40 tries, the others in none. In games that were won, the median loss was between 125 and 550 troops. The easy stage invites a relaxed style, and that goal asks for the opposite. We wrote down a suggestion to loosen it, but have not changed it.

## What bots cannot tell us

Bots have no input delay, so their win rates are only good for comparing stages with each other. And a real player who gets a warning and then uses Ink to turn the game around would count as a false alarm in this table, though the warning was useful. **[unverified]** how it feels in a human hand.

## FAQ

### How often does Inkisle's crisis warning cry wolf?

In 3,360 bot games it warned before a win only 3 times, 0.14% of 2,096 wins, against a limit of 10%. Each of the three was a boss stage.

### Does it catch every lost game?

No. It warned in only 20.7% of lost games, on purpose, so that it speaks only when sure.

### Do bot results tell us how players will feel?

Not directly. Bots have no input delay and do not use Ink in a crisis, so the numbers only compare stages. How it feels in a human hand is unverified.
