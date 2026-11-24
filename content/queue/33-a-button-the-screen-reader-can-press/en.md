---
title: A button the screen reader can press
description: Inkisle’s close icon and lighthouse had spoken labels, but their accessibility actions were missing. We checked both the words and what happens when you activate the control.
slug: a-button-the-screen-reader-can-press
lang: en
category: making-of
keywords: Inkisle, accessibility, screen reader, interface, widget tests
image_alt: An X and a lighthouse icon on two small cards, with focus rings around both controls.
---

Inkisle is an island-conquest strategy game in development. During an accessibility pass, we examined how the game describes its controls to a screen reader. Two controls stood out: the X that closes a panel and the lighthouse on the chart that replays an ending. We’re developing the game for iOS.

## From a name to an action

The two controls already had names. In Flutter’s accessibility tree, the node with the name had lost its tap action when we replaced the icon’s default description. We attached the action to the same node as the label. In the tests, activating Close dismisses the panel and activating the lighthouse opens the ending.

## Hearing it once

We also checked what gets read twice. A fleet ratio button was exposing the same percentage in the label and in the visible text. The intro’s Skip control and the numbered chart markers had similar duplication. We kept one spoken label in each case, with the information a player needs to identify the control.

## FAQ

### Has this been tested with a screen reader on a phone?

The widget tests checked the labels and accessibility actions. We have not verified the changes on a phone with VoiceOver or TalkBack.

### What does the lighthouse let you do?

Activate the lighthouse on the chart to replay an ending.
