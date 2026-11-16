---
title: Two free seas and one unlock: how we simplified payment
description: Inkisle keeps seas 1 and 2 free and opens the rest with one purchase, Unlock All Seas. Why we dropped the consumable ink shop, how the lock is computed in code, the lines we drew on restore and refunds, and what we have not tested.
slug: two-free-seas-and-one-unlock
lang: en
category: making-of
keywords: Inkisle, in-app purchase, non-consumable, free seas, restore purchases, mobile game
image_alt: Two open islands, then a row of islands with padlocks behind them, and one key lying across the row.
---

Inkisle, our island-conquest strategy game for iOS, now keeps seas 1 and 2 free and opens seas 3 to 30 (28 seas) with one purchase, Unlock All Seas. We dropped the consumable ink shop and kept the six tip items. The store product itself has not been created yet, so nothing can be bought today. The game is in development and not released, and this post does not state a price or a date.

## What changed

The first design had every stage free, with ink that lowers difficulty sold as small consumable items. On November 15 the owner changed it. **Seas 1 and 2 are free, Unlock All Seas is a one-time non-consumable purchase, and ink is no longer sold.** Ink is now earned only through stars: one for every 5 stars, and 2 for beating a boss. Ink bought earlier still works.

## The lock is computed

The number of locked seas is not typed into the code. It is the number of seas minus the number of free seas. Today that is 30 − 2 = 28, and when seas are added the purchase sheet text "opens N seas" follows. The sales copy we prepared promises that new seas are included.

- On the chart, stages from sea 3 on carry a red padlock, and tapping one opens the shop instead of the stage.
- Buying or restoring opens them all.
- After a win, if the next stage is in a locked sea, the game returns to the chart.

## The app has to behave without a product

If the store has no product yet, or the price lookup fails, only the buy button turns off and a "coming soon" note appears. The app does not break. The price is looked up again each time the sheet opens, so when the product exists it works with no code change. That is exactly where we are now. Product setup is blocked on the store side, so we have never run the real purchase flow.

## Lines we drew on purpose

| Case | Behavior |
|---|---|
| A player who already got past sea 2 | Locked. Records and stars stay, and a purchase or restore opens them again |
| Another device | Progress arrives through iCloud but the unlock does not. Tap "Restore purchases" there |
| Refunds | We do not take access back |
| TestFlight "open all" | Removes the progress lock but not the payment lock, so the purchase flow can be tested in the sandbox |

Not taking access back after a refund is both a choice and a limit. Flutter's `in_app_purchase` package has no state that reports a refund, and at this scale we decided not to verify receipts on a server. That judgment is an estimate [unverified].

## What we have not checked

- We have not bought or restored on a real device [unverified]. So far there are widget tests (padlock, shop, purchase, unlock) and a check of the StoreKit configuration.
- The 375px and 320px renders were covered by widget tests, not by a simulator [unverified].
- Android uses the same code path, but with no product registered we could not test payment there [unverified].
- Purchase text in the 11 languages other than Korean is machine-translated [unverified].

## FAQ

### How much of Inkisle is free?

Seas 1 and 2. The other 28 seas open together once Unlock All Seas is bought. The game is not released yet.

### How many times do I have to buy?

Once. It is a non-consumable purchase, designed to include new seas as well.

### Do tips affect the game?

No. The six tip items give no advantage in the game and stay as they are.
