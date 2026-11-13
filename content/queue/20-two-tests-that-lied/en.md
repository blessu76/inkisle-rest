---
title: Two tests that lied: a screen size and a language that leaked
description: Phone-sized tests quietly ran with a tablet-sized screen, and two tests left the language setting behind for the next ones. How both showed up and what fixed them, with no change to the app itself.
slug: two-tests-that-lied
lang: en
category: making-of
keywords: Inkisle, Flutter, widget tests, test isolation, random test order, mobile development
image_alt: Two small phone outlines side by side, one with a crooked ruler beside it.
---

Two of the Flutter widget tests for Inkisle, our island-conquest strategy game for iOS, passed for the wrong reason. Phone-sized tests quietly ran with a 2400 by 1800 view, and two tests left the language setting behind for the tests after them. We fixed both without changing the app. The game is still in development and not released.

A test that passes for the wrong reason is worse than a test that fails. Two of ours did exactly that.

## The screen that was not the size we said

### What was wrong

To test a phone layout we set the test surface to, say, 375 wide and the pixel ratio to 1. We assumed the app then saw a 375-wide screen. It did not: the view's physical size stayed at its default of **2400 by 1800**, so the screen size the app read (MediaQuery) was false. On tablets the app overrides MediaQuery with its own scaling, so those tests were fine. On phones it does not, so phone tests were lying.

### How it showed up

It stayed hidden until the harbor sheet started to decide portrait or landscape from MediaQuery. Then **29 phone tests** failed at once. We fixed the three layout test files that mattered by setting the view's physical size to match the surface (and resetting it afterwards). The sheet now reads the width the route gives it instead.

The catch: **38 other test files** only change the surface, so their MediaQuery may still be false. The rule we wrote down: a new layout decision made from MediaQuery will fall into the same trap.

## The language that stayed behind

### What was wrong

The tests run with the UI language fixed to Korean. Two tests that loop over all languages ended with the setting cleared (the device language) instead of back to Korean. A settings-sheet test that ran after them could not find its Korean label.

### How it showed up

In the normal order this was invisible, because those two sat at the end of their file. Random order showed it: with seeds 20261111, 7777 and 424242 we got 8, 5 and 3 failures. The fix was a setUp that resets the language for every test and a tear-down in the two tests. After it, all three seeds pass (1794 tests, 7 skipped) and the app code did not change at all.

One detail worth keeping: Flutter runs each test file in its own isolate, so random order only shuffles tests inside one file. Any test that changes a global setting should restore it when it finishes.

## What we have not done

We checked the other globals we know of (Ink lock ticks, carried speed, keychain timeout and a few more) and they restore properly. We have not found a way to catch the MediaQuery trap automatically. **[unverified]** that no other test hides behind it.

## FAQ

### Why did Inkisle's phone-sized tests use the wrong screen size?

Setting the test surface did not change the view's physical size, which stayed at 2400 by 1800, so MediaQuery was false on phones. We now set the physical size to match and reset it afterwards.

### Did the app itself change?

No. Both problems were in the tests. After the fix all three random seeds pass, 1794 tests with 7 skipped.

### Is every test now safe from the screen-size trap?

Not proven. 38 other test files only change the surface, so their MediaQuery may still be false, and we have no automatic check yet.
