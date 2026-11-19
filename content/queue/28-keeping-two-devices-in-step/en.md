---
title: Keeping two devices in step: moving iCloud sync into a shared app kit
description: Inkisle's progress, ink and settings were already matched across devices through iCloud. On November 16 we moved that bridge into a shared app kit. How we kept saved data intact, the merge rules that never shrink, how the purchase mark is handled, and what we have not checked on real devices.
slug: keeping-two-devices-in-step
lang: en
category: making-of
keywords: Inkisle, iCloud, cross-device sync, save data, merge, mobile game
image_alt: Two screens of different sizes joined by a thin thread, with the islands on both charts painted the same colors.
---

In Inkisle, our island-conquest strategy game for iOS, progress, ink and key settings (language and nickname) are matched across devices on the same Apple ID through the player's own iCloud key-value storage. That sync already existed. What we did on November 16 was not to build it but to move a bridge we had written ourselves into a shared app kit, and the biggest worry was not losing a single saved value. We have not yet checked a round trip between a real iPhone and iPad [unverified]. The game is in development and not released.

## What we moved

The owner's instruction that day was that syncing game data between Apple devices should be mandatory, and that it should go into the shared app kit. We found the iCloud key-value entitlement already switched on, and a Swift bridge plus a storage wrapper of our own running inside the app. So:

| Part | What changed |
|---|---|
| Bridge | Deleted our own Swift bridge and wrapper, and switched to the kit's platform storage: iCloud on iOS, local-only elsewhere |
| Keys and encoding | Kept the storage keys, the string encoding and the storage identifier as they were |
| Before reading | On iOS, wake the sync once just before a read (sync carries on if that fails) |
| Project settings | Added the iCloud capability to the project file as well |

## Not losing data

Because keys and formats stayed the same, the new build reads what the old build wrote, and the old build reads what the new one writes. We pinned both directions with tests: reading an old-format chunk with the new code, reading a new chunk with the old code, and reading an old settings chunk. Only code was deleted; saved values were not touched.

## Merging never shrinks

When two devices hold different progress, we kept the app's own merge. The kit has a merger too, but we did not use it. The app's merge already only grows, and keeping the same keys and format was safer with it left alone.

- Stars and best records per stage take the larger value.
- Progress takes whichever device went further, and ink and settings only combine, never shrink.
- If the value in the cloud differs from what we last pushed, we push again, to recover from an old build that overwrote the same key.

## What happened to the purchase mark

An earlier post said that the unlock does not carry to another device. This work changed that. The sync chunk now carries a mark that "Unlock All Seas" was bought, and another device that reads it opens too. The mark **only grows.** A chunk without it does not take it away; we push it again.

This is a design change following the owner's "mandatory sync" instruction, and it has one limit: once the mark is synced, a refund does not withdraw it on other devices. How to treat refunds is left as a policy decision. The purchase flow itself has not been run on a real device either [unverified].

## Size and tests

iCloud key-value storage has a total limit (1 MB). The sync chunk for a save with all 240 stages cleared is about 6.3 KB, and a test keeps it under 16 KB. The 14 new tests cover unchanged keys and encoding, merging two devices, the purchase mark spreading and never being withdrawn, staying local when offline or signed out, and merging after coming back online. Across the four cloud test files, 77 tests passed.

## What we have not checked

- **A real sync between an iPhone and an iPad has not been checked [unverified].** It can only be seen on real devices or TestFlight.
- Deletions do not travel to other devices, because this sync only merges.
- Android does not apply. Data stays on the device.
- If an old build on another device overwrites the same key, the purchase mark can briefly disappear, and the new build pushes it again.
- The privacy policy now describes this sync: game data is kept in the player's own iCloud, not on our servers, and can be turned off in the device settings.

## FAQ

### Is Inkisle progress stored on a server?

No. It is matched across devices on the same Apple ID through the player's own iCloud key-value storage, and not sent to our servers.

### Can sync be turned off?

Yes. Turning off this app's iCloud in iOS settings stops the sync and leaves the data on the device only.

### Does it sync on Android?

No. On Android data stays on the device.
