---
title: One shape and one color per sea: how the chart marks what you cleared
description: On the sea chart, stages you have not cleared stay white everywhere, and cleared ones take the shape and color of their sea. The rule, the fourteen styles, the contrast check and how we looked at a wide screen.
slug: one-shape-per-sea
lang: en
category: making-of
keywords: Inkisle, sea chart, UI design, color contrast, accessibility, mobile game
image_alt: A row of stage markers on a sea chart, white circles first, then colored shapes: a diamond, a hexagon, a shield.
---

On Inkisle's sea chart, our island-conquest strategy game for iOS, a stage you have not cleared stays white everywhere, and a cleared stage takes the shape and color of its sea. There are fourteen sea styles, all with a white number that passes a 4.5 contrast check. The game is still in development and not released.

On the sea chart every stage is a marker with a number. We wanted the chart to show progress at a glance, without a progress bar: what you have cleared should look different from what is still ahead.

## The rule

| State | Look |
|---|---|
| Not cleared | white fill, ink outline, ink number (a circle; a boss is a rounded square) |
| Locked | the same, with a grey outline and a grey padlock |
| Current | white, with a thicker outline in the color of that sea |
| Cleared | the shape and color of that sea, white number |
| Cleared boss | the same shape, plus an inner white ring |

A boss is drawn a little bigger (64 instead of 56). We kept those sizes because the code that bends the route assumes a radius of 32.

## Fourteen sea styles

### Shapes and colors

Seas 1 to 14 each have their own shape: circle, rounded square, diamond, hexagon, octagon, pentagon, shield, scallop, oval, ink blot, plus, burst, drop and ticket. Each also has its own color, and from sea 15 the list starts again. A test pins that all fourteen differ.

### Contrast and fit

Every color has to carry a white number, so we check contrast: all fourteen are at 4.5 or better (between 4.53 and 17.2). The drop and the shield push the number slightly down, since their middle sits lower. A test also checks that a number box fits inside every shape, and that "13-10" and "14-10" stay on one line even at 320 px wide.

## Looking at it

We drew all fourteen shapes in a gallery at 320 and 375 px, and charts for a few seas. The app has no web target, so for a 1280 px width we rendered the chart in a test instead: markers spread sideways, the row spacing (92 px) stays, and a number check puts every marker, with its tap area, inside the width at 1280 and at 768.

## What we have not checked

- Test fonts draw some text as blocks, so real labels in Korean or Arabic at those widths are not verified by that test. **[unverified]**
- We looked at only a few of the 18 wide chart images by eye, and we have not run it in a real window.
- Whether people read "color = my progress" without being told is something only players can say.

## FAQ

### How does Inkisle's sea chart show what you have cleared?

Uncleared stages are white circles, and a cleared stage takes the shape and color of its sea, with a white number. A cleared boss gets an inner white ring.

### Are the colors readable?

All fourteen sea colors have a contrast of 4.5 or better against the white number, between 4.53 and 17.2.

### Has it been checked on a real device?

No. We checked it in rendered tests and galleries, at 320, 375, 768 and 1280 wide. Real labels in Korean or Arabic are not verified.
