---
title: A playable prototype in a day
description: Sixteen stages, two seas and one HTML file of about 95 KB with no outside requests. How the prototype is built, what we tested in a headless browser, and what we could not test.
slug: a-playable-prototype-in-a-day
lang: en
category: making-of
keywords: Inkisle, prototype, web prototype, deterministic game engine, HTML game, mobile game, canvas
image_alt: Many small islands with troop numbers and a fleet crossing the sea in the Inkisle prototype.
---
Before building an app we wanted something playable on a phone. On 2026-10-29 we built a web prototype in a single day. This post describes what is in it, how it is put together, and, just as important, what we could not check.

![Three phone screens from the prototype: the sea chart with a stage card, a battle with a drag in progress, and a victory result with three stars. The text in the screenshots is Korean.](/assets/posts/img/proto-shots.jpg)
*The sea chart with a stage card, a battle with a drag in progress, and the result screen.*

## What is in it

- **Sixteen stages:** sea 1, "Calm Bay", has eight, and sea 2, "Windy Strait", has eight. Further seas show up as locked cards.
- **The loop:** chart, stage card, battle, result with one to three stars, next stage.
- **Unlocking:** beat a stage and the next opens. Beat the boss and the next sea opens. Stars never block progress; they are for extra goals.
- **Sound:** synthesized in the browser, with a different pentatonic scale for each sea and a note that rises with every capture in a chain.
- **Progress** is saved in the browser's local storage, and the game still works in memory if storage is blocked.

## How it is built

- **One file.** About 95 KB, with no outside requests and no web fonts, so it runs offline and inside a frame.
- **Engine and screen are separate.** The engine is a pure module with no DOM, no clock and no random calls. The interface only queues commands such as "send 50% from island 0 to island 1", and a loop steps the engine every 100 ms.
- **Speed-up works by stepping faster**, not by changing the rules, so star time limits stay fair at 2x.
- **Pause** stops the ticks, and the game pauses itself when the tab is hidden.

Keeping the engine pure was a bet on the future: the same code can later run turn by turn over a network, and a recorded command list can replay a match.

## What we tested

We drove the prototype with a headless Chrome. On a 375 by 812 screen it started from empty storage, sent fleets by mouse drag and by touch drag, paused (the tick counter stayed frozen), won stage 1-1 in about 12 seconds with three stars, saved progress, unlocked 1-2 and kept progress after a reload. At 320 by 568 nothing overflowed sideways. The browser console showed no errors.

We also ran a deterministic check: the same map and commands gave the same result on every run, and running in real time and in turns gave the same outcome.

## What we could not test

- **Real devices.** iOS Safari and a mid-range Android phone are **not checked**. A headless browser's touch emulation is not a finger.
- **Performance.** Our target is 22 islands and 300 fleets at 60 frames per second. It has not been measured.
- **Missing features:** a free-play mode, a way to export play logs, mid-stage saving, and several animations.
- **Known rough edges:** the drag label can cover a neighbor's number, and the stage card can cover nodes on the chart.

The next steps are a 30-minute test with five to eight people, with a play log built in first. The next post is about the balance work we did without humans.
