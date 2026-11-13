---
title: A sea chart that changes its road: one line style per sea
description: With 14 seas on one scrolling chart, the road between stages looked the same everywhere. We gave each sea its own line style, color and wiggle, made the angle continue across sea borders, and only draw what is on screen. The values, the tests, and what we have not seen on a phone.
slug: a-chart-that-changes-its-road
lang: en
category: making-of
keywords: Inkisle, sea chart, level map, route style, mobile UI, Flutter, rendering performance
image_alt: A winding dotted road between islands that changes from a rope line to a wave line, drawn in soft vector colors.
published: 2026-11-12T19:00+09:00
---
The chart is the screen where you spend the quiet time between battles: a long road of stages. With 14 seas, the road looked the same all the way. A long scroll with no change feels like one sea repeated. So each sea got its own road.

## What changes per sea

| Sea | Line | Color of a cleared road |
|---|---|---|
| 1 | solid (as before) | coral |
| 2 | rope | sail beige |
| 3 | long dashes, faint | lighthouse white |
| 4 | wave | teal |
| 5 | beads | coral pink |
| 6 | long dashes | sand gold |
| 7 | thick solid | navy |
| 8 | thin solid | cobalt |
| 9 | beads | lantern gold |
| 10 | thick solid | gold |
| 11 | brush | ink |
| 12 | double line | silver |
| 13 | wave | white sail |
| 14 | beads | deep ink |

Each sea also has its own sway (how far the road swings sideways and how often). Seven line types are shared across the 14 seas, and the colors are all different. The road leading to a stage is drawn in the style of the sea that stage belongs to. After sea 14 the styles repeat, as a placeholder.

## Two things that were not about looks

- **No jump at sea borders.** The sway is one continuous function, so the angle continues where one sea ends and the next begins, and the islands do not jump sideways.
- **Draw only what is visible.** The chart will have hundreds of stages, so islands and roads outside the visible area are skipped. In a widget test, drawing ten visible roads took under 16 ms.

## Decorations came after

A second step added small marks along the road per sea: knots, brackets, footprints, stars, ink drops. In seas 7, 10 and 11 we then changed these to a whirl, a beacon and a spread, and the sea 14 drop to a pointed one.

## Tests

Seven tests check that every sea has a style, that the sway stays under .32, that the 14 colors are all different, that every line type is used, that a cleared road has a contrast of at least 3:1 against its edge, that islands stay inside 18% to 82% of the width at 320 px, and that every sea draws different pixels. The first sea's layout does not move.

## What we have not checked

- All renders so far are test captures, where the font is a block. We have not looked at it on a real iPhone or Android phone. **[unverified]**
- We did not measure the frame time with all 800 stages, only the ten-road check. **[unverified]**
- On the dark night seas (11 and 14), the ink-colored road is held up by a white edge. Whether it looks right is a design check we still owe.
- The game is in development and is not released.

## FAQ

### How many sea road styles does Inkisle have?

Seven line types are shared across the 14 seas, and each sea has its own color and sway. After sea 14 the styles repeat as a placeholder.

### Does the sea chart jump sideways at sea borders?

No. The sway is one continuous function, so the angle continues across borders and the islands do not jump.

### Has the chart been tried on a real phone?

Not yet. All renders so far are test captures, and the game is still in development, not released.
