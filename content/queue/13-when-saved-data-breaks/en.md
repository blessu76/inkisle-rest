---
title: When saved data breaks: how the app recovers
description: A phone can lose, truncate or block an app's saved data. How Inkisle handles missing, damaged, outdated and unavailable storage for progress, the intro and the sound setting, and where our recovery is still blunt.
slug: when-saved-data-breaks
lang: en
category: making-of
keywords: Inkisle, save data, error handling, robustness, local storage, mobile game, versioned save
image_alt: A small notebook with one torn page next to a row of islands, a calm way to show a damaged save.
---
Inkisle has no accounts and no server, so all progress lives **only on the phone**. That makes the saved data simple, and it also means nobody can restore it for you. The question we asked: what should the app do when what it reads back is wrong?

## Four things that can go wrong

| Situation | What the app does |
|---|---|
| Nothing saved yet | Start from stage 1-1 |
| Saved text is damaged (cannot be read) | Treat it as empty, start fresh |
| Saved by a different version of the format | Ignore it, start fresh |
| The phone's storage cannot be opened at all | Play in memory; nothing breaks, but nothing is kept after closing |

The saved data carries a version number in its name and in its content, so a future change to the format can be recognized instead of misread.

## Damage to one part does not wipe the rest

The progress record has one entry per stage. Our review pointed out that a single damaged entry used to reset everything. Now each stage is read on its own: an unreadable entry is skipped and the other stages are kept. Only a completely unreadable file, or a different version, means a fresh start. Entries also have to say the stage was **won**, because only wins are ever written.

## A repair that repairs

The intro keeps its own small save (the shuffled bag from an earlier post). When that was damaged, reading failed before the app wrote anything new, so the broken text stayed there and the problem repeated at every launch. The fix: if reading fails, start from the default and **write the default over it**. The intro code has tests for broken saves.

## Settings fall back to the quiet choice

The only setting is sound. If its saved data is broken, the answer is **off**, not on. A broken file should never make the game louder.

## Progress can only grow

Stars and best times are only ever improved, and a lost replay changes nothing. The unlock rule looks only at whether the previous stage was won.

## What we have not checked

- We tested damaged text, wrong versions and missing storage in code. We have **not** tested a phone that is out of space or an operating-system backup and restore.
- When the whole file is unreadable, the player starts again from stage 1-1. For a player with many stars that would feel bad, and we have not decided whether to add something gentler.
