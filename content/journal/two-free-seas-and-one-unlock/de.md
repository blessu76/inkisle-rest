---
title: Zwei kostenlose Meere und eine Freischaltung: wie wir die Bezahlung vereinfacht haben
description: Inkisle hält die Meere 1 und 2 kostenlos und öffnet den Rest mit einem einzigen Kauf, Alle Meere freischalten. Wie verbrauchbare Tinte im Verkaufsangebot eingerichtet ist, wie die Sperre im Code berechnet wird, welche Grenzen wir bei Wiederherstellung und Erstattungen gezogen haben und was wir noch nicht geprüft haben.
slug: two-free-seas-and-one-unlock
lang: de
translation_of: en
category: making-of
keywords: Inkisle, In-App-Kauf, nicht verbrauchbar, kostenlose Meere, Käufe wiederherstellen, Mobile Game
image_alt: Zwei offene Inseln, dahinter eine Reihe Inseln mit Vorhängeschlössern, und ein Schlüssel quer über der Reihe.
published: 2026-11-19T19:17+09:00
---

Inkisle, unser Strategiespiel über die Eroberung von Inseln für iOS, hält die Meere 1 und 2 kostenlos und öffnet die Meere 3 bis 30 (28 Meere) mit einem einzigen Kauf, Alle Meere freischalten. Verbrauchbare Tinte (Pakete zu 5 und 15) ist im Verkaufsangebot enthalten, aber nicht veröffentlicht und auf einem Gerät nicht geprüft. Die sechs Trinkgeld-Artikel bleiben. Die Store-Produkte sind im Registrierungsschritt, aber noch nicht zur Prüfung eingereicht und auf einem Gerät nicht geprüft; ob der Kauf funktioniert, ist daher noch nicht bestätigt. Das Spiel ist in Entwicklung und nicht veröffentlicht. Dieser Beitrag nennt weder Preis noch Datum.

## Was sich geändert hat

Der erste Entwurf machte alle Stufen kostenlos, und Tinte, die den Schwierigkeitsgrad senkt, wurde in kleinen verbrauchbaren Artikeln verkauft. Am 15. November hat der Verantwortliche das geändert. **Die Meere 1 und 2 sind kostenlos, Alle Meere freischalten ist ein einmaliger nicht verbrauchbarer Kauf.** Verbrauchbare Tinte (Pakete zu 5 und 15) ist im Verkaufsangebot enthalten, aber nicht veröffentlicht und auf einem Gerät nicht geprüft. Tinte gibt es außerdem über Sterne: eine für je 5 Sterne und 2 für den Sieg über einen Boss. Früher gekaufte Tinte funktioniert weiterhin.

## Die Sperre wird berechnet

Die Zahl der gesperrten Meere steht nicht fest im Code. Sie ergibt sich aus der Anzahl aller Meere minus der Anzahl der kostenlosen Meere. Heute sind das 30 − 2 = 28. Kommen Meere hinzu, passt sich der Text im Kaufblatt „öffnet N Meere“ an. Der Verkaufstext, den wir vorbereitet haben, verspricht, dass neue Meere enthalten sind.

- In der Karte tragen Stufen ab Meer 3 ein rotes Vorhängeschloss, und ein Tipp darauf öffnet den Shop statt der Stufe.
- Kauf oder Wiederherstellung öffnet alle.
- Nach einem Sieg kehrt das Spiel zur Karte zurück, wenn die nächste Stufe in einem gesperrten Meer liegt.

## Die App muss ohne Produkt funktionieren

Wenn der Store noch kein Produkt hat oder die Preisabfrage fehlschlägt, wird nur der Kaufbutton deaktiviert, und ein Hinweis „demnächst verfügbar“ erscheint. Die App stürzt nicht ab. Der Preis wird bei jedem Öffnen des Blatts neu abgefragt, sodass er ohne Codeänderung funktioniert, sobald das Produkt existiert. Genau da stehen wir jetzt. Die Einrichtung des Produkts ist auf Store-Seite blockiert, deshalb haben wir den echten Kaufablauf noch nie durchgespielt.

## Bewusst gezogene Grenzen

| Fall | Verhalten |
|---|---|
| Spieler, der Meer 2 bereits hinter sich hat | Gesperrt. Fortschritt und Sterne bleiben, ein Kauf oder eine Wiederherstellung öffnet sie erneut |
| Anderes Gerät | Fortschritt kommt über iCloud, die Freischaltung nicht. Dort auf „Käufe wiederherstellen“ tippen |
| Erstattungen | Wir entziehen den Zugang nicht |
| TestFlight „Alle öffnen“ | Entfernt die Fortschrittssperre, aber nicht die Zahlungssperre, damit der Kaufablauf in der Sandbox getestet werden kann |

Den Zugang nach einer Erstattung nicht zurückzunehmen ist Entscheidung und Grenze zugleich. Das Flutter-Paket `in_app_purchase` hat keinen Zustand, der eine Erstattung meldet, und in dieser Größenordnung haben wir entschieden, Belege nicht auf einem Server zu prüfen. Diese Einschätzung ist eine Schätzung **[ungeprüft]**.

## Was wir nicht geprüft haben

- Wir haben nicht auf einem echten Gerät gekauft oder wiederhergestellt **[ungeprüft]**. Bisher gibt es Widget-Tests (Vorhängeschloss, Shop, Kauf, Freischaltung) und eine Prüfung der StoreKit-Konfiguration.
- Die Darstellungen mit 375 px und 320 px wurden durch Widget-Tests abgedeckt, nicht durch einen Simulator **[ungeprüft]**.
- Android nutzt denselben Code-Pfad, aber ohne registriertes Produkt konnten wir dort die Zahlung nicht testen **[ungeprüft]**.
- Der Kauftext in den 11 Sprachen außer Koreanisch ist maschinell übersetzt **[ungeprüft]**.

## Häufige Fragen

### Wie viel von Inkisle ist kostenlos?

Die Meere 1 und 2. Die übrigen 28 Meere öffnen sich gemeinsam, sobald Alle Meere freischalten gekauft ist. Das Spiel ist noch nicht veröffentlicht.

### Wie oft muss ich kaufen?

Einmal. Es ist ein nicht verbrauchbarer Kauf, der so gedacht ist, dass auch neue Meere enthalten sind.

### Beeinflussen Trinkgelder das Spiel?

Nein. Die sechs Trinkgeld-Artikel bringen im Spiel keinen Vorteil und bleiben, wie sie sind.
