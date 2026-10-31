---
title: Art direction: three mockups, one pick
description: We asked for the same battle screen from our design assistant (two directions) and from GPT. What each returned, what went wrong with the outside mockup, and why minimal vector won.
slug: art-direction-grace-vs-gpt
lang: en
category: making-of
keywords: Inkisle, art direction, minimal vector, mockup, GPT, game UI, mobile game art
image_alt: Four phone-sized mockups side by side: two of the minimal vector direction, one low 3D diorama, one outside GPT mockup.
published: 2026-10-31T19:09+09:00
---
The brief for the look was one sentence: a **premium minimal vector** style, "graphics a bit more upscale", on a phone screen held upright. A flat, readable look suits a game whose whole point is numbers on islands.

## What we asked for

The same two screens from each source: a **battle screen** (islands, fleets, the ratio bar) and a **sea chart screen** (stages as nodes, stars, the next sea). Mockups only, no game code.

- **Our design assistant, Grace**, produced two directions. **A** is minimal vector: soft shapes, one gentle shadow, ink-blot progress on the chart. **B** is a low 3D diorama, where only the islands get depth.
- **GPT** was asked for the same battle screen as an outside opinion.
- We also asked a third model, but its first two replies were generic RPG and lobby screens unrelated to the brief, so we dropped it.

![Left to right: direction A battle screen, direction A sea chart, direction B battle screen with 3D islands, and GPT's battle screen. The text inside the screenshots is Korean.](/assets/posts/img/art-compare.jpg)
*Left to right: A battle, A chart, B battle, GPT battle. The captions inside the images are Korean.*

## What came back

- **A** read best at a glance. Islands are blobs in one color each, numbers are big, and a captured island fills with its new color. Each side also has its own flag shape, so the game still reads without color vision.
- **B** looked richer in a still image, but the 3D depth made the numbers compete with the island shapes, and it would cost more to draw and to keep readable at small sizes.
- **GPT's** battle mockup came back with the island shapes missing: only routes and numbers floated on the sea, and the reply was cut off because of a length limit on what we could pass along. We asked again for the chart screen and did not get a usable one in time. That is a limit of our process, not a verdict on the model.

## The pick, and what it means

We picked **A**. It is the cheapest to draw, the easiest to read at 320 px wide, and it matches the rule of the game: color is the reward.

Two cautions. This was **one round**, judged by a small team, with no players involved. And a mockup is not a game: A has since been built into the prototype, which is where it will really be tested. The next post is about that prototype.
