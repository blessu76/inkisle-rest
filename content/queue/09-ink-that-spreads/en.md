---
title: Ink that spreads: the small effects that say what just happened
description: In Inkisle a captured island leaves a bloom of ink, a comeback shows a banner, and the last enemy island lights up. What each effect is for, how long it lasts, and how the first-run finger hint works.
slug: ink-that-spreads
lang: en
category: making-of
keywords: Inkisle, game feel, visual feedback, mobile game, onboarding hint, animation
image_alt: A coral ink bloom spreading over a captured island while fleets move between other islands.
---
In a game about turning the map your color, the moment that matters most is **an island changing hands**. If it is only a color swap, it is easy to miss on a small screen. So we added a few small effects whose job is to say "this just happened".

## The capture bloom

When an island changes owner, an **ink bloom** spreads from it in the new owner's color and fades out. It lasts about **0.75 seconds**. The shape is an irregular blob drawn the same way as the blooms in the intro, so the game and its opening look related. A test checks that a capture leaves a bloom and that it disappears afterwards.

## Three moments that get a message

- **A comeback.** When you were behind and take the lead, a banner appears **once**. It shows for about 1.6 seconds. "Once" matters: a banner that fires every time the lead flips back and forth turns into noise.
- **The last island.** When the enemy is down to **its last island**, that island is highlighted so you know where to aim.
- **Finishing a sea.** Clearing a whole sea has its own short moment, separate from the result sheet of a single stage.

## The first-run finger hint

A new player does not know that you drag from one island to another. In a stage the first time, a small **finger sweeps from your island to the nearest other island**. It disappears as soon as you send anything, and a test checks that. We kept it small and short so a player who already knows the control is not slowed down.

## What we have not checked

- All of this is covered by tests for **when** an effect appears, not for **how it feels**. Timing, size and color are first guesses and have not been tried on a real phone by anyone outside the team.
- We do not know yet whether the comeback banner is encouraging or just distracting.
