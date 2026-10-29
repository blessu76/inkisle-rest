---
title: Three stars, one rule: how a stage is rated
description: Every stage in Inkisle can earn up to three stars. What each star means, why stars never block progress or go down, the 13 kinds of three-star goals, and the wrong label we found and fixed.
slug: three-stars-one-rule
lang: en
category: making-of
keywords: Inkisle, star rating, game progression, game design, mobile game, replayability
image_alt: A row of three stars, the first two filled in coral and the third one an outline.
---
Each of Inkisle's 16 stages gives one to three stars. Stars are the game's way of saying "you can do better" without forcing you to. Here is the rule, and one mistake we made in explaining it.

## What each star means

1. **★1: win.** You beat the stage.
2. **★2: win within the stage's time limit.** Every stage has its own limit.
3. **★3: the stage's own goal.** A different goal for the stage, shown on its card.

The game decides these three conditions in one place, and the screens only ask it for the result. That sounds obvious, but when we first wrote the chart and the result sheet, pieces of the rule had leaked into both. A review found it, and we moved the checks into small helper functions next to the rule, so if the rule changes there is one place to change.

## Stars never get in the way

- **Stars do not unlock anything.** Winning a stage opens the next one. Beating the boss opens the next sea.
- **Stars never go down.** Replay a stage and lose, and nothing is recorded. Replay and win, and the game keeps the best of everything: a star once earned stays, and the best time is kept.

So a replay can only help you.

## Thirteen kinds of three-star goals

The ★3 goal is different in almost every stage. There are 13 kinds so far, for example:

- lose at most a number of troops,
- win without ever sending 100%,
- take every empty island,
- never lose a single island,
- capture a fortress in one attack,
- hold off a simultaneous enemy attack once,
- do not attack the enemy's home island before a given time.

Each goal is written in plain words in the app, for example "Win without sending 100%."

## The wrong label

The ★1 label first read "**win while keeping your islands**." But the condition was only "win": you could lose islands and still get the star. The label promised something the game did not check. A review caught it, and the label is now simply "**win**".

## What we have not checked

- The time limits for ★2 were set by the prototype and, as the bot test in an earlier post showed, look **too generous** for bots. We do not know yet what human times look like.
- We do not know whether players will feel that 13 different goals are interesting or just confusing.
