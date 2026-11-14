---
title: Not a stretched phone: giving Inkisle its own iPad layout
description: On an iPad the battle screen used to be the phone screen made bigger. How the board got side panels in landscape, why a 9.7-inch iPad needed narrower ones, and what we have and have not checked.
slug: not-a-stretched-phone
lang: en
category: making-of
keywords: Inkisle, iPad layout, landscape, responsive UI, mobile game, game design
image_alt: A tablet in landscape showing a board of islands in the middle with a narrow panel on each side.
published: 2026-11-14T17:30+09:00
---

Inkisle, our island-conquest strategy game for iOS, now has an iPad layout of its own: in landscape the battle screen has a panel on each side of the board, and in portrait the bars stop stretching. A 9.7-inch iPad needed narrower panels than the larger ones. The game is still in development and not released.

Inkisle was drawn for a phone held upright. An iPad was allowed to run it, but the battle screen was simply the phone screen made bigger: the bars ran to the edge and landscape was not supported. We decided a tablet should get a layout of its own, not a stretched one.

## What changed

- **Four orientations on iPad.** Phones stay portrait. iPads can now be turned any way.
- **A three-part battle screen in landscape** (when the width is 640 or more). A left panel always shows the title, the time, the Ink and the star goal. The board keeps its own proportions in the middle. A right panel holds the ratio control, drawn as a tall pill 54 high.
- **Portrait iPad** keeps one column, but the ratio bar is capped at 520 wide and the choice bar at 560, so nothing stretches across the whole screen.
- Chart, settings, harbor, shop, result card, intro and ending already had width limits and were left as they were.

## The small iPad

### Side panels

The side panels are 200 wide. On a 9.7-inch iPad in landscape the usable width is about 683 by 512, and two panels leave a board only about 283 wide. So below a width of 760 the panels shrink to 168. The 11-inch and 13-inch iPads keep 200.

### The harbor sheet

The harbor sheet had a similar problem. In landscape it was one column, and the intro text, the Ink refill and the close button used so much height that you saw only about one and a third cards. On a landscape tablet it is now two columns: the shelf on the left (440 wide), the rest on the right. Phones in landscape keep one column.

## One thing a screenshot found

On the night sea, the star goal in the left panel was dark text on dark water. It now uses the same color as the title. A widget test covers the fix, but we did not shoot it again on a build. **[unverified]**

## What we checked

- Layout tests: 10 sizes (from 9.7-inch to 13-inch, portrait and landscape) across the screens, 64 cases. Phones at 375 and 320 wide have no side panels, and a test checks that.
- Simulator runs on a 13-inch and an 11-inch iPad, 40 screenshots in the first round and 20 more in landscape later. We looked at some of them by eye: nothing overlapped or was cut off.
- Not checked: Android tablets, and the two-column harbor sheet on a simulator (only in a rendered test image). **[unverified]**

## FAQ

### Does Inkisle have an iPad layout?

Yes. On iPad, Inkisle's battle screen has a three-part landscape layout and a width-limited portrait layout. It is a work in progress and has not been released.

### Why did a 9.7-inch iPad need narrower side panels?

In landscape its usable width is about 683, so two 200-wide panels would leave a board about 283 wide. Below a width of 760 the panels shrink to 168.

### Does Inkisle run on Android tablets?

Android is developed alongside iOS, but we have not checked Android tablets for this layout.
