---
title: Wenn gespeicherte Daten kaputtgehen: wie sich die App erholt
description: Ein Handy kann die gespeicherten Daten einer App verlieren, abschneiden oder blockieren. Wie Inkisle mit fehlendem, beschädigtem, veraltetem und nicht verfügbarem Speicher bei Fortschritt, Intro und Soundeinstellung umgeht und wo unsere Wiederherstellung noch grob ist.
slug: when-saved-data-breaks
lang: de
translation_of: en
category: making-of
keywords: Inkisle, Speicherdaten, Fehlerbehandlung, Robustheit, lokaler Speicher, Mobile Game, versionierter Spielstand
image_alt: Ein kleines Notizbuch mit einer eingerissenen Seite neben einer Reihe von Inseln, eine ruhige Art, einen beschädigten Spielstand zu zeigen.
---
Inkisle hat keine Konten und keinen Server, daher liegt der gesamte Fortschritt **nur auf dem Handy**. Das macht die gespeicherten Daten einfach, und es heißt auch, dass sie niemand für dich wiederherstellen kann. Unsere Frage: Was soll die App tun, wenn das, was sie zurückliest, falsch ist?

## Vier Dinge, die schiefgehen können

| Situation | Was die App tut |
|---|---|
| Noch nichts gespeichert | Bei Level 1-1 beginnen |
| Der gespeicherte Text ist beschädigt (nicht lesbar) | Als leer behandeln, neu anfangen |
| Von einer anderen Version des Formats gespeichert | Ignorieren, neu anfangen |
| Der Speicher des Handys lässt sich gar nicht öffnen | Im Arbeitsspeicher spielen; nichts geht kaputt, aber nach dem Schließen bleibt nichts erhalten |

Die gespeicherten Daten tragen eine Versionsnummer in ihrem Namen und in ihrem Inhalt, sodass eine künftige Änderung des Formats erkannt statt falsch gelesen werden kann.

## Schaden an einer Stelle löscht nicht den Rest

Der Fortschrittseintrag hat einen Eintrag pro Level. Unser Review wies darauf hin, dass ein einziger beschädigter Eintrag früher alles zurücksetzte. Jetzt wird jedes Level für sich gelesen: Ein unlesbarer Eintrag wird übersprungen, die anderen Level bleiben erhalten. Nur eine komplett unlesbare Datei oder eine andere Version bedeutet einen Neuanfang. Außerdem muss ein Eintrag besagen, dass das Level **gewonnen** wurde, weil nur Siege geschrieben werden.

## Eine Reparatur, die wirklich repariert

Das Intro führt einen eigenen kleinen Spielstand (den gemischten Beutel aus einem früheren Beitrag). Wenn er beschädigt war, schlug das Lesen fehl, bevor die App etwas Neues schrieb. Der kaputte Text blieb also stehen, und das Problem wiederholte sich bei jedem Start. Die Lösung: Schlägt das Lesen fehl, wird mit dem Standardwert begonnen und der **Standardwert darübergeschrieben**. Der Intro-Code hat Tests für kaputte Spielstände.

## Einstellungen fallen auf die leise Wahl zurück

Die einzige Einstellung ist der Ton. Sind ihre gespeicherten Daten kaputt, lautet die Antwort **aus**, nicht an. Eine kaputte Datei sollte das Spiel nie lauter machen.

## Fortschritt kann nur wachsen

Sterne und Bestzeiten werden nur verbessert, und eine verlorene Wiederholung ändert nichts. Die Freischaltregel prüft nur, ob das vorherige Level gewonnen wurde.

## Was wir nicht geprüft haben

- Wir haben beschädigten Text, falsche Versionen und fehlenden Speicher im Code getestet. Ein Handy ohne freien Speicherplatz oder die Sicherung und Wiederherstellung des Betriebssystems haben wir **nicht** getestet.
- Ist die ganze Datei unlesbar, beginnt der Spieler wieder bei Level 1-1. Für jemanden mit vielen Sternen würde sich das schlecht anfühlen, und wir haben nicht entschieden, ob wir etwas Sanfteres hinzufügen.
