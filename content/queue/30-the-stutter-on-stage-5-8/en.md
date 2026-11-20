---
title: The stutter on stage 5-8: it was the screen, not the game engine
description: Stage 5-8 in Inkisle felt choppy. We measured before touching anything, found that the cost sat in screen drawing rather than the game rules, and cut a frame's cost from 3.4 to 1.3 ms on a computer. What we changed, what we left alone, and what we have not checked on a phone.
slug: the-stutter-on-stage-5-8
lang: en
category: making-of
keywords: Inkisle, performance, stutter, frame time, game design, mobile game, optimization
image_alt: Four tall purple bars on the left and four short coral bars on the right, with an arrow between them and a dashed line marking the budget.
---

Inkisle, our island-conquest strategy game for iOS, felt choppy on stage 5-8 during testing. The easy guess was that the game engine, the part that moves fleets and decides captures, had grown too heavy. We measured first. The engine was not the problem; the screen around it was. After the change, the cost of one frame on stage 5-8 dropped from 3.4 ms to 1.3 ms on our computer. The game is in development and not released, and these numbers do not come from a phone.

## What we measured

A frame has two kinds of work: the game rules moving one tick forward, and the screen being built and drawn. On stage 5-8 one tick of the rules cost only 3 to 5 microseconds on average. The screen cost about a thousand times more.

Most of that screen cost came from three things:

1. **The whole heads-up display was rebuilt every frame.** The game controller announced a change every frame, so the power bars, goal text, result sheet, ratio bar, badges, pick bar, crisis overlay and tide button were all rebuilt, even when nothing in them had changed. About 2.5 ms of the 3.4 ms went to building widgets.
2. **Number labels missed their cache.** The cache key included the exact transparency and size of each number, and those change continuously during a capture swell or a fade. So every frame produced fresh layouts, and when the cache passed 600 entries it was cleared whole, so one frame had to lay out everything again. Draw time at the slowest 1 percent of frames was 5 to 10 times the average.
3. **Small repeated work.** Each fleet looked up its ink color twice, every island position and radius was recalculated for every fleet, and one shader cache used a text key.

## What we changed

- The heads-up display now listens to a small signal that fires only when something it shows has changed, such as the tick, pause, speed, crisis state, goals or hints. Painting still happens every frame, as before.
- Number labels are rounded to coarse steps (transparency in 32 steps, size in quarter pixels) so the cache is hit, and when it fills up only the older half is removed.
- Repeated lookups are computed once per frame, and the shader key became a record instead of a string.

The size and transparency rounding is not visible to the eye.

## The numbers

These are measured on a computer, at a 375 × 667 screen, in a mode that is only good for comparing before and after.

| | before | after |
|---|---|---|
| Stage 5-8 whole frame, mean | 3,433 µs | 1,267 µs |
| Stage 5-8 whole frame, slowest 1% | 10,803 µs | 5,182 µs |
| Stage 5-8 drawing, mean | 818 µs | 201 µs |
| Stage 5-8 drawing, slowest 1% | 4,540 µs | 1,284 µs |

A 60 frames-per-second game has about 16.6 ms per frame, so even before the change the work fit in that budget on a computer. That is why the choppiness we felt may have another cause too (see below).

## What we left alone

We did not change a single line of the rules or the balance code. Only the screen layer changed: how the controller announces updates, which widgets listen, and the drawing caches. The same seed still produces the same 600-tick result, and the existing checks for golden images, deterministic play and bot simulations stayed green.

We also left one real cost for later. The crisis forecast runs on the screen thread: on the heaviest stage we measured, stage 17-3, it averaged 3.4 ms and its slowest 1 percent reached 11.8 ms, which can cause a small hitch every half second. Spreading that work over several frames would give the same result, but it risks changing decisions, so we did not do it now. On stage 5-8 it costs 0.17 ms and does not matter.

## What we added

A headless benchmark for the engine, and a performance test with loose upper limits. It catches the kind of regression where cost explodes with fleet count or where each frame allocates too much. We kept the limits loose on purpose, because tight ones would fail whenever the test machine is busy. By default the heaviest of these tests are skipped, and they run only when asked.

## What we have not checked

- **Frame rate on a real phone, at 60 or 120 frames per second, is unchecked.** Our numbers are screen-thread cost on a computer, not graphics cost on a device.
- **The fog veil and band layers are not measured and not changed.** They are drawn with a full-screen blur, which costs the graphics chip rather than the processor. If stage 5-8 still stutters on a phone, this is our first suspect.
- We did not look at a browser render at 320, 375, 768 and 1280 px, because no layout changed.
- That input feels more responsive is only our expectation.

## FAQ

### Why did stage 5-8 stutter in Inkisle?

Our measurement pointed at the screen being rebuilt and number labels being laid out again every frame, not at the game rules. We fixed those; real-phone frame rates are not yet checked.

### Did the optimization change how the game plays?

No. We did not touch the rules or the balance code, and the same seed gives the same result as before.

### Is the game still choppy on a phone?

We do not know yet. Our numbers come from a computer. We will check on a real device in TestFlight.
