---
title: Versionshinweise in der App: ein Blatt in 12 Sprachen und eine Längenprüfung
description: Die Versionshinweise von Inkisle sind ein Blatt in den Einstellungen, keine Webseite. Wie die Hinweise jedes Builds in 12 Sprachen geschrieben werden, die Prüfungen von Anzahl und Länge der Einträge und der Testfehler, der ein leeres Blatt anzeigte.
slug: release-notes-inside-the-app
lang: de
translation_of: en
category: making-of
keywords: Inkisle, Versionshinweise, Lokalisierung, mehrsprachig, Tests, Mobile Game
image_alt: Ein Blatt Papier, das vom unteren Bildschirmrand nach oben steigt, darüber eine Reihe von zwölf kleinen Sprachreitern.
---

Die Versionshinweise von Inkisle, unserem Strategiespiel über die Eroberung von Inseln für iOS, sind ein Blatt in der App, das über die Einstellungen geöffnet wird, keine Webseite. Die Hinweise jedes Builds werden in 12 Sprachen geschrieben, und ein Prüfskript kontrolliert die Anzahl der Einträge und ihre Länge. Die Prüfung von Build 34 meldete 0 Fehler und 0 Warnungen. Das Spiel ist noch in Entwicklung und nicht veröffentlicht.

## Wir haben die Webseite entfernt

Anfangs hatte der Hauptbildschirm einen Link „Versionshinweise“ und eine Info-Schaltfläche (ⓘ). In Build 32 haben wir beides entfernt. Was im Info-Fenster stand (Datenschutzerklärung, Nutzungsbedingungen, Version, Open-Source-Lizenzen, Betreiber, Kontakt und der Hinweis ab 16 Jahren), wanderte in die Einstellungen, und die Versionshinweise wurden zu einem Blatt, das über eine Zeile „Versionshinweise“ dort geöffnet wird. Die Seite mit den Versionshinweisen auf der Website haben wir am 15. November ebenfalls entfernt. Ohne eigene Website ist der Text in der App die einzige Quelle.

Das Blatt nutzt denselben Rahmen wie unsere anderen Popups (InkSheet). Es nimmt höchstens 60 % der Bildschirmhöhe ein, die Titelzeile und das Schließen-X (48×48) bleiben fest, und nur der Inhalt scrollt innerhalb des Blatts.

## Ein Build, eine Datei, 12 Sprachen

Für jeden Build enthält `release_notes/<build>.json` einen Titel, eine Einleitung und die Einträge in 12 Sprachen (ko, en, ja, zh-Hant, es, pt-BR, fr, de, id, th, vi, tr). Die Dateien werden in `assets/release_notes.json` gebündelt, das mit der App ausgeliefert wird, und das Blatt liest es von dort.

## Prüfungen von Länge und Anzahl

Ein Prüfskript liest die Dateien und meldet Regelverstöße.

- **RN06:** Ein Eintrag darf höchstens 200 Zeichen lang sein. Der deutsche Text war zu lang, deshalb wurde der Saisonabschluss-Eintrag in Build 34 auf 183 Zeichen gekürzt. In Build 31 haben wir einen Kauf-Eintrag in zwei geteilt, um die Grenze einzuhalten.
- **RN05:** Empfohlen werden 3 bis 6 Einträge. Das ist nur eine Warnung und blockiert keine Veröffentlichung. Die verbleibenden Warnungen betreffen alte Builds mit 1 oder 2 Einträgen; sie sind eine ehrliche Aufzeichnung dessen, was geschrieben wurde, deshalb haben wir sie belassen.
- Ein Test schlägt fehl, wenn es keinen Eintrag für die aktuelle Version und Build-Nummer gibt. Jede Build-Erhöhung braucht also zuerst den Hinweis in 12 Sprachen.
- Das iOS-Upload-Skript führt die Prüfung der Versionshinweise vor dem grünen Gate aus (Format, Analyse, Tests).

## Der Test, der ein leeres Blatt sah

Zwei Tests des Versionshinweis-Blatts sahen plötzlich ein leeres Blatt. Die Ursache lag im Test, nicht in der App. Das Bundle ist eine echte Asset-Datei, und mit wachsender Größe endete `pumpAndSettle`, das wartet, bis der Bildschirm zur Ruhe kommt, bevor das Lesen der Datei fertig war. Wir haben die Tests so geändert, dass sie das Blatt öffnen, 300 ms mit `runAsync` warten und dann neu zeichnen. Der App-Code hat sich nicht geändert.

## Was wir nicht geprüft haben

- Übersetzungen außer Koreanisch und Englisch sind maschinell erstellt und noch nicht von Muttersprachlern geprüft **[ungeprüft]**.
- Wir haben das Blatt auf einem echten Gerät nicht bei 60 % Höhe gesehen. Widget-Tests bei 375×667 und 320×568 stehen dafür **[ungeprüft]**.

## Häufige Fragen

### Wo finde ich die Versionshinweise von Inkisle?

In der App die Zeile „Versionshinweise“ in den Einstellungen antippen, dann öffnet sich ein Blatt. Eine eigene Webseite gibt es nicht. Das Spiel ist noch nicht veröffentlicht.

### In wie vielen Sprachen sind sie geschrieben?

In 12 Sprachen. Außer Koreanisch und Englisch sind sie maschinell übersetzt und noch nicht geprüft.

### Was passiert, wenn ein Eintrag zu lang ist?

Überschreitet ein Eintrag 200 Zeichen, meldet das Prüfskript einen Fehler, und wir kürzen ihn oder teilen ihn in zwei.
