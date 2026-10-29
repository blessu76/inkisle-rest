---
title: What the app does not have: no ads, no accounts, no tracking
description: Some of Inkisle's design is about what is left out. The app asks for no account and has no ads or tracking tools, it runs on iOS and Android from one codebase, and we drew a new icon for both. What we decided and what we have not checked.
slug: what-the-app-does-not-have
lang: en
category: making-of
keywords: Inkisle, privacy, no ads, no account, app icon, iOS, Android, Flutter, mobile game
image_alt: A coral island drawn as a simple ink blot on a cream background, the Inkisle app icon.
---
A lot of what makes an app feel good is what it does **not** do. For the first release of Inkisle we decided on a short list of things to leave out.

## No account, no ads, no tracking

- **No account.** You open the app and play. There is no sign-up and no sign-in.
- **No ads and no tracking tools.** The app's list of outside packages is short: one to save small settings on the phone, one to play sounds, and one to open a web page. It also includes a package for the icon font, which has nothing to do with tracking. There is no advertising package, no analytics package and no sign-in package in it.
- **Progress stays on the phone.** The saved stars and the sound setting are stored locally and are not sent anywhere.

The app has an information screen with a link to the privacy policy, which is the same page that is on this website. The one thing that touches the network is opening that page, and it only happens when the player taps it.

## One codebase, two platforms

Inkisle is built with Flutter, so **iOS and Android are developed together** from the same code. Every change goes through code formatting, static analysis and automated tests on that shared code. The plan is to start with one platform first. We still build and test Android the whole time, so that it does not become a second project later. The game is locked to portrait orientation on both. The minimum versions are iOS 13 and Android API level 24.

## The icon

The icon is a simple **coral ink island** on a cream background. One piece of drawing code generates three files:

- the normal square icon for iOS and older Android,
- the Android "adaptive" foreground, drawn inside the 66% safe area that Android crops to,
- a one-color silhouette for Android 13's themed icons.

We shipped a bug here and fixed it: the adaptive icon was being shrunk twice (once by us and once by the build settings), so it looked too small on Android. Now the shrink happens in one place only.

## What we have not checked

- We have not run the app on a **real iPhone or Android phone** from a store build, and we have not submitted it to either store. Things like store review, in-app screens in other languages and how the icon looks on different launchers are still open.
- "No tracking" describes what is in our own code and package list. We have not audited the packages we depend on beyond reading their descriptions.
