---
title: A drag that forgives: the small rules behind one gesture
description: Sending a fleet in Inkisle is one drag. The small rules that make it work with a real finger: a wider pick area, a drag that samples the whole path, one finger at a time, and clear messages when a send is not possible.
slug: a-drag-that-forgives
lang: en
category: making-of
keywords: Inkisle, touch controls, mobile game UX, drag and drop, multitouch, game design
image_alt: A thumb dragging from a coral island across the sea to a neighboring island, with a dotted line behind it.
---
The first stage teaches the whole control in one line: **drag an island onto another island and a ship leaves**. That sentence hides a lot of small decisions, because a thumb is much blunter than a mouse. This post collects the ones we are most sure about.

## The finger is bigger than the island

An island on screen can be smaller than a fingertip, and the finger covers it while you aim. So when you pass over islands during a drag, the area that counts as "on this island" is **the island's radius plus 12 pixels**. Without the extra margin, a drag that visibly ended on an island often missed it.

## A fast swipe cannot skip an island

When you sweep across several islands to pick them, the screen only reports your finger every so often. A fast swipe could jump from one side of an island to the other without ever being reported inside it. The game therefore **samples along the line** between two reports, so every island the finger crossed is counted.

## One finger at a time

Our first code review found a case we had not thought of: if a **second finger** touches the screen in the middle of a drag, the second touch replaced the first one, and the two fingers' movements got mixed up. That could leave the selection in a strange state or send a fleet nobody meant to send. The fix is simple: the game follows **only the first finger** and ignores the others until it lifts. A test covers the second finger being ignored.

## Say why nothing happened

If you try to send from an island that has too few troops, the send does not happen. Silence feels like a bug, so the game shows a short message: an island needs **at least 2 troops** to send. Pressing and holding an island for **0.4 seconds** selects all of your islands, and a message tells you to tap or drag to a target for an all-out attack.

## The amount to send

How much leaves an island is set by a ratio bar. The default is **50%**. Stage 1-2 teaches choosing the ratio, and its three-star goal is to win **without ever sending 100%**, which nudges you to try the other settings.

## What we have not checked

- Everything here is checked with simulated touches in tests. We have **not watched real people** use it on real phones, and the gestures that look fine in a test can still feel wrong.
- The sizes (12 px, 0.4 s) are first guesses. They will change if players miss islands or select all by accident.
