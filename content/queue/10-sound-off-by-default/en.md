---
title: Sound that is off by default: a scale for each sea
description: Inkisle starts silent and the player turns sound on. How the sounds are made in code with no audio files, how each sea gets its own five-note scale, and why a chain of captures climbs the scale.
slug: sound-off-by-default
lang: en
category: making-of
keywords: Inkisle, game audio, procedural sound, pentatonic scale, mobile game, accessibility, settings
image_alt: Five rising notes drawn as small ink dots above a row of islands.
---
Many people play on a phone in public or in bed. A game that starts loud is a game that gets closed. So in Inkisle **sound is off until the player turns it on**, and that setting is saved.

## Off really means off

When sound is off, the audio code is not even started: the sound player is created the first time a sound is actually needed. A muted game never touches the phone's audio system. If the saved setting is damaged or storage fails, the answer is "off" again. The app also respects the phone's silent switch. Errors inside the audio code are caught instead of leaking out, which was a fix after a code review found that one kind of audio error could escape the safety net.

## No sound files

Every sound is **made in code**. The app builds a short 16-bit mono WAV at 22,050 samples per second for each tone: a wave (sine, triangle or sawtooth), a 12 ms attack and an exponential decay. There are no recorded files to license. The tone parameters come from the web prototype, so the app sounds like the prototype did.

## A scale for each sea

Each sea has its own **pentatonic scale**, five notes that sound fine in any order:

| Sea | Steps above the base note (semitones) |
|---|---|
| Calm Bay | 0, 2, 4, 7, 9 |
| Windy Strait | 0, 2, 5, 7, 9 |

The base note is 523.25 Hz. The second sea differs in one note, the third step (5 instead of 4).

## Chains climb

When you capture several islands in a row, **each capture is one step higher** in the sea's scale. After five steps the scale wraps up an octave, and above the tenth step it stays on the top note. A good chain is therefore audible as a rising line, and because the scale has only notes that fit together, a fast chain stays in tune.

## What we have not checked

- The tests check the notes and that muted means silent. They cannot tell us whether it **sounds pleasant**. Nobody outside the team has listened on a real phone speaker or headphones.
- These tones are plain beeps. Whether they stay as the final sound or get replaced is not decided.
