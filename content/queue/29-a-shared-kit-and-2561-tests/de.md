---
title: Was wir beim Upgrade eines gemeinsamen Kits schützen: ein Gate mit 2.561 Tests
description: Jedes Mal, wenn Inkisle das gemeinsame Kit unserer Apps aktualisiert, muss es ein Gate aus Format, Analyse und vollständigem Test bestehen. Warum wir keine ganze Kit-Funktion ersetzt haben, wie Zeittests unter Last wackelten, welche Dateien sich beim letzten Upgrade geändert haben und was wir nicht geprüft haben.
slug: a-shared-kit-and-2561-tests
lang: de
translation_of: en
category: making-of
keywords: Inkisle, gemeinsames Kit, Tests, Game Center, Upgrade, Mobile Game
image_alt: Mehrere kleine Blöcke gleicher Form in einem Rahmen, über die ein einzelner grüner Punkt wandert.
---

Inkisle, unser Strategiespiel über die Eroberung von Inseln für iOS, nutzt ein gemeinsames Kit, auf das sich mehrere unserer Apps stützen. Jedes Mal, wenn wir die Version des Kits erhöhen, führt ein Gate vor dem Commit Format, statische Analyse und die vollständige Testsuite aus. Am 19. November haben wir das Kit von 0.15.2 auf 0.15.3 gehoben: Das Gate bestand 2.561 Tests (8 übersprungen), und nur zwei Dateien änderten sich, `pubspec.yaml` und `pubspec.lock`. Dieser Beitrag handelt davon, wie diese Zahl gehalten wird und was dabei gewackelt hat. Das Spiel ist in Entwicklung und nicht veröffentlicht.

## Das Gate hat drei Schritte

Ein Skript führt sie vor einem Commit der Reihe nach aus: Die Code-Formatierung darf sich nicht ändern, die statische Analyse muss 0 Probleme melden, und alle Tests müssen bestehen. Schlägt einer fehl, committen wir nicht. Wenn jemand anderes sagt „es ist durchgelaufen“, führen wir es vor dem Commit selbst noch einmal aus.

## 14. November: Wir haben nicht die ganze Kit-Funktion ersetzt

Mit dem Wechsel des Kits von 0.12.0 auf 0.13.0 konnte es den Spitznamen und die Game-Center-Bestenliste übernehmen. Die Vorgabe des Verantwortlichen war, dass jedes Spiel beim ersten Start einen Spitznamen festlegen lässt und in der Game-Center-Bestenliste erscheint. Wir haben **nicht die gesamte Spielerfunktion des Kits übernommen.** Wir hatten vier Gründe, unsere eigene Version für besser zu halten:

1. Der Spitzname liegt im Einstellungsdatensatz, der sich über iCloud zwischen Geräten synchronisiert. Ihn in den Speicher des Kits zu verschieben, würde diese Synchronisierung brechen.
2. Wir haben bereits ein Spitznamen-Blatt in 16 Sprachen und Tests, die über Kombinationen aus Sprache und Bildschirmgröße eingefroren sind.
3. Die Bestenlisten sind 24 dynamische Listen, deren Werte aus dem synchronisierten Fortschrittsdatensatz abgeleitet werden. Ein Umzug würde zwei Orte hinterlassen, die eine Bestleistung speichern.
4. Android Play Games braucht weiterhin die Bibliothek, die es nutzt.

Also zog nur die iOS-Game-Center-Anbindung in das Kit um, und die Board-IDs, gespeicherten Spitznamen und Bestleistungen blieben unverändert erhalten. Das erneute Senden eines Rückstands nach spätem Anmelden und das Vorausfüllen des Spitznamens mit dem Game-Center-Namen kamen gleichzeitig dazu. Wir haben 10 Tests hinzugefügt, und das Gate bestand danach 1.990 Tests (7 übersprungen).

## Zeittests wackelten

Zweimal wackelte in diesem Gate ein Test, der Zeit misst, unter Last. Ein Frame-Budget-Test, der 800 Straßen zeichnet, schlug einmal fehl, als die Tests parallel liefen, und während der iCloud-Arbeit schlug ein Performance-Budget-Test einmal fehl. Beide bestanden, als sie allein oder als die ganze Suite erneut lief. Wir deuten das als Last, nicht als unsere Änderung [ungeprüft; die Ursache haben wir nicht nachverfolgt]. Die Budgets haben wir nicht gelockert.

## 19. November: zwei Dateien geändert

Version 0.15.3 lässt die öffentliche API, wie sie war; sie lässt eine Neuzählung in der iCloud-Synchronisierung nach dem Abbau stoppen und ergänzt Dokumentation. In der App haben wir weder Code noch Tests geändert. Die Größenbegrenzung, die die App verwendet (512 KB), ist beabsichtigt, deshalb haben wir sie beibehalten. Die geänderten Dateien waren `pubspec.yaml` und `pubspec.lock`, und das Gate bestand beim ersten Durchlauf, diesmal ohne Zeit-Wackeln. Die Testzahl wuchs von 1.990 am 14. November auf 2.561.

## Was wir nicht geprüft haben

- **Game-Center-Anmeldung, Punkteübermittlung, Bestenlisten-Bildschirm und ein iCloud-Roundtrip wurden nicht auf einem echten Gerät geprüft [ungeprüft].** Wir schauen in TestFlight nach.
- Die Darstellungen mit 375 px und 320 px wurden durch Widget-Tests bei 320×568 abgedeckt, nicht direkt angesehen [ungeprüft].
- Die Ursache der unter Last wackelnden Tests haben wir nicht gefunden [ungeprüft].
- Die Zahlen hier sind die Gate-Ergebnisse dieses Tages, und die Testzahl wird sich später ändern.

## Häufige Fragen

### Was ist das gemeinsame Kit?

Ein Bündel Code, das mehrere unserer Apps gemeinsam nutzen. Inkisle nutzt davon die Teile für Spitzname, Game Center und iCloud-Synchronisierung.

### Was prüft ihr beim Upgrade des Kits?

Ein Skript prüft, dass sich die Formatierung nicht ändert, dass die statische Analyse 0 Probleme meldet und dass alle Tests bestehen. Schlägt einer fehl, committen wir nicht.

### Ist das Spiel veröffentlicht?

Nein. Es ist noch in Entwicklung und nicht veröffentlicht.
