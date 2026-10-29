---
title: A ten-second intro in three versions: sky, sea and land
description: Inkisle opens with a ten-second intro that comes in three versions. How the three share one ending, why a shuffled bag decides which one you see, when it shortens to three seconds, and what happens with reduce-motion turned on.
slug: three-ten-second-intros
lang: en
category: making-of
keywords: Inkisle, game intro, app launch, skip button, reduce motion, accessibility, mobile game
image_alt: Islands in a mint-green sea with coral ink spreading across one of them, the opening image of the Inkisle intro.
---
The first thing you see when you open Inkisle is an intro. We wanted it to feel like a small event the first few times and to **get out of the way** after that. This post describes how the intro is built and the rules that decide what you see.

## One ending, three beginnings

The full intro is **10 seconds**. The first 7 seconds come in three versions, **sky**, **sea** and **land**. The last 3 seconds are the same in all of them: the ending that leads into the menu. Keeping the ending shared means we draw it once, and every version arrives at the same place.

## Which one do you get?

Picking at random can show the same intro three times in a row, which feels like a bug. So the app uses a **shuffled bag**: it puts all three versions in a bag in random order and takes one out at each launch. When the bag is empty it is refilled. Two consequences:

- Within one round, **three launches in a row show all three versions**.
- The first version of a new round is never the same as the last one you saw.

The bag is saved on the phone, so it keeps working between launches.

## Long first, short later

For the **first three launches** you get the full 10 seconds. From the fourth launch on, the app plays only the shared ending, **3 seconds**. A skip button appears **0.6 seconds** after the intro starts, so a first-time viewer is not asked to skip before seeing anything. Skipping calls the same "done" step as the intro finishing, and a test checks that it runs only once.

## Reduce motion

If the phone's reduce-motion setting is on (iOS "Reduce Motion", or animations turned off on Android), the intro does **not move**. It shows the finished ending frame for **1.2 seconds** and goes to the menu. The skip button is there from the start.

## When the saved bag is broken

Our code review found that a damaged saved bag was never repaired: the app failed to read it, started over on every launch, and kept showing the full 10-second version. The fix is to treat unreadable data as "no data" and write a fresh one right away. If storage is not available at all, the app picks a random version and plays the full intro, and it never blocks starting the game. There are tests for these cases.

## What we have not checked

- We have not measured how the intro runs on a **real phone**. The tests cover the rules above, not the animation's smoothness.
- Whether ten seconds is the right length for a first launch is a guess until other people see it.
