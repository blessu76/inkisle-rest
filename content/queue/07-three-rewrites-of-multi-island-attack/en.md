---
title: Sending from several islands at once: three rewrites of one control
description: Attacking one island from several of yours was the hardest control in Inkisle. The first drag-based version, the tap-to-select fix and the swipe-to-select version, and what each one taught us.
slug: three-rewrites-of-multi-island-attack
lang: en
category: making-of
keywords: Inkisle, touch controls, mobile game UX, multi-select, drag and drop, game design, iteration
image_alt: A battle where several islands send fleets toward one enemy island.
---
Sending one fleet is easy: drag from your island to the target. The hard part of Inkisle's controls is **sending from several islands at once**, because late stages are won by arriving together. We rewrote that control three times in a few hours, and the story shows why.

## v0.1: everything at once

The first prototype supported several ways to do it:

- Drag from an island to a target, and **pass over your other islands on the way** to add them as sources.
- **Long-press** (0.4 seconds) an island to select all of yours, then drag for an all-out attack.
- Tap a source, then tap the target, as an alternative to dragging.

On paper it covered everything. In practice a thumb covers the very island it is passing over, and a stage that taught "pass over islands while dragging" asked for a gesture that is hard to see and hard to aim.

## v0.1.1: select first, then go

The fix was to split the gesture in two. **Tap your islands one by one to select them**, then tap the target and they all depart. Dragging a selected island still sends the whole group. We added:

- a small badge above the selection that shows how many islands are picked,
- a tap on empty sea to clear the selection,
- a wider pick area when joining while dragging (island radius plus 12 px), since a finger is bigger than an island,
- a hint shown the first few times, plus the stage cards that teach the control now describe tapping.

Tapping is precise and calm, but with many islands it is **many taps** before every attack. In a real-time game, that is time.

## v0.1.2: sweep to pick

The newest version lets you **swipe across your islands to pick them in one stroke**, then choose the target. Selecting four islands is now one motion instead of four taps. Whether the earlier methods remain as fallbacks, and how the sweep feels in detail, are not final **[unverified at the time of writing]**.

## What we learned, and what we do not know

- **A gesture that needs the finger to land on a small target while moving is fragile on a phone.** The first fix removed the aiming; the second removed the repeating.
- Each version fixed one problem and exposed the next, which is normal, but it also means the control is still unsettled.
- We have **no data from outside players** on any of the three versions. The exact feel of v0.1.2 is **[unverified]** until others try it.

The test with five to eight people is where this control will really be judged. If they still hesitate before an attack, we will change it a fourth time.
