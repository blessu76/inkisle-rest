---
title: Ein spielbarer Prototyp an einem Tag
description: Sechzehn Stages, zwei Meere und eine HTML-Datei von etwa 95 KB ohne externe Anfragen. Wie der Prototyp aufgebaut ist, was wir im Headless-Browser getestet haben und was wir nicht testen konnten.
slug: a-playable-prototype-in-a-day
lang: de
translation_of: en
category: making-of
keywords: Inkisle, Prototyp, Web-Prototyp, deterministische Spiele-Engine, HTML-Spiel, Mobile Game, Canvas
image_alt: Viele kleine Inseln mit Truppenzahlen und eine Flotte, die im Inkisle-Prototyp das Meer überquert.
---
Bevor wir eine App bauen, wollten wir etwas auf dem Handy Spielbares haben. Am 2026-10-29 haben wir an einem einzigen Tag einen Web-Prototyp gebaut. Dieser Beitrag beschreibt, was darin steckt, wie er aufgebaut ist und, ebenso wichtig, was wir nicht prüfen konnten.

![Drei Handybildschirme des Prototyps: die Seekarte mit einer Stage-Karte, ein Kampf mit einem laufenden Ziehen und ein Siegesergebnis mit drei Sternen. Der Text in den Screenshots ist Koreanisch.](/assets/posts/img/proto-shots.jpg)
*Die Seekarte mit einer Stage-Karte, ein Kampf mit einem laufenden Ziehen und der Ergebnisbildschirm.*

## Was drin ist

- **Sechzehn Stages:** Meer 1, „Ruhige Bucht" (Calm Bay), hat acht, und Meer 2, „Windstraße" (Windy Strait), hat acht. Weitere Meere erscheinen als gesperrte Karten.
- **Die Schleife:** Karte, Stage-Karte, Kampf, Ergebnis mit ein bis drei Sternen, nächste Stage.
- **Freischalten:** Schließt man eine Stage ab, öffnet sich die nächste. Besiegt man den Boss, öffnet sich das nächste Meer. Sterne blockieren nie den Fortschritt; sie sind Zusatzziele.
- **Sound:** im Browser synthetisiert, mit einer eigenen pentatonischen Tonleiter für jedes Meer und einem Ton, der mit jeder Eroberung in einer Kette höher steigt.
- **Der Fortschritt** wird im lokalen Speicher des Browsers gesichert, und das Spiel funktioniert weiter im Arbeitsspeicher, wenn der Speicher blockiert ist.

## Wie er aufgebaut ist

- **Eine Datei.** Etwa 95 KB, ohne externe Anfragen und ohne Webfonts, sodass er offline und in einem Frame läuft.
- **Engine und Bildschirm sind getrennt.** Die Engine ist ein reines Modul ohne DOM, ohne Uhr und ohne Zufallsaufrufe. Die Oberfläche stellt nur Befehle wie „50 % von Insel 0 nach Insel 1 schicken" in eine Warteschlange, und eine Schleife schaltet die Engine alle 100 ms weiter.
- **Das Beschleunigen funktioniert, indem schneller weitergeschaltet wird**, nicht indem die Regeln geändert werden, sodass die Zeitlimits für Sterne bei 2x fair bleiben.
- **Pause** hält die Ticks an, und das Spiel pausiert von selbst, wenn der Tab verborgen wird.

Die Engine rein zu halten war eine Wette auf die Zukunft: Derselbe Code kann später Zug um Zug über ein Netzwerk laufen, und eine aufgezeichnete Befehlsliste kann ein Match wiedergeben.

## Was wir getestet haben

Wir haben den Prototyp mit einem Headless-Chrome gesteuert. Auf einem Bildschirm von 375 mal 812 startete er mit leerem Speicher, schickte Flotten per Maus-Ziehen und per Touch-Ziehen los, pausierte (der Tick-Zähler blieb eingefroren), gewann Stage 1-1 in etwa 12 Sekunden mit drei Sternen, speicherte den Fortschritt, schaltete 1-2 frei und behielt den Fortschritt nach einem Neuladen. Bei 320 mal 568 lief nichts seitlich über. Die Browser-Konsole zeigte keine Fehler.

Außerdem haben wir eine deterministische Prüfung gemacht: Dieselbe Karte und dieselben Befehle ergaben bei jedem Lauf dasselbe Ergebnis, und der Lauf in Echtzeit und der rundenweise Lauf führten zum gleichen Ausgang.

## Was wir nicht testen konnten

- **Echte Geräte.** iOS Safari und ein Android-Handy der Mittelklasse sind **nicht geprüft**. Die Touch-Emulation eines Headless-Browsers ist kein Finger.
- **Performance.** Unser Ziel sind 22 Inseln und 300 Flotten bei 60 Bildern pro Sekunde. Das wurde nicht gemessen.
- **Fehlende Funktionen:** ein freier Spielmodus, eine Möglichkeit, Spielprotokolle zu exportieren, Speichern mitten in einer Stage und mehrere Animationen.
- **Bekannte Ecken und Kanten:** Das Ziehen-Label kann die Zahl einer Nachbarinsel verdecken, und die Stage-Karte kann Knoten auf der Seekarte verdecken.

Die nächsten Schritte sind ein 30-Minuten-Test mit fünf bis acht Personen, wobei zuvor ein Spielprotokoll eingebaut wird. Der nächste Beitrag handelt von der Balancing-Arbeit, die wir ohne Menschen gemacht haben.
