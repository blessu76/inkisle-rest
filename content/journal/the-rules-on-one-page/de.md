---
title: Die Regeln auf einer Seite: Inseln, Truppen, Eroberung
description: Alle Regeln von Inkisle auf einer Seite: wie Inseln Truppen erzeugen, wie Flotten fliegen, wie die Eroberung berechnet wird und wie eine Partie endet. Startwerte, vor den Tests.
slug: the-rules-on-one-page
lang: de
translation_of: en
category: making-of
keywords: Inkisle, Spielregeln, Inseleroberung, deterministische Engine, Spieldesign, Eroberungsregeln
image_alt: Inseln mit Truppenzahlen und gepunkteten Routen, auf denen Flotten zwischen ihnen reisen.
published: 2026-10-30T05:40+09:00
---
Gute Strategiespiele lassen sich in einer Minute erklären. Dies ist unser Versuch, die Regeln von Inkisle auf einer Seite zu erklären. **Jede Zahl hier ist ein Startwert aus dem Designdokument.** Wir erwarten, einige davon nach den Tests zu ändern, und die späteren Beiträge dieser Serie zeigen, welche sich schon geändert haben.

## Inseln erzeugen Truppen

- Jede Insel, die du besitzt, bringt **1 Truppe pro Sekunde** (ein „Tick“ sind 100 ms, also eine Truppe alle 10 Ticks).
- Es gibt eine **Obergrenze** von 45. Darüber hinaus produziert die Insel nicht mehr, und überschüssige Truppen aus Verstärkungen fließen mit 1 pro Sekunde auf die Obergrenze zurück. So verhindert das Spiel, dass du alles auf einer Insel stapelst und wartest.
- **Neutrale Inseln produzieren nicht.** Ihre Zahl ist fest, sie liest sich also wie ein Preisschild.
- Du startest mit einer Heimatinsel mit 20 Truppen. Der Gegner meist auch, und wenn nicht, steht es auf der Stufenkarte.

## Flotten entsenden

Ziehe von einer deiner Inseln zu einer anderen Insel und lass los. Eine Leiste unten wählt den Anteil: **25, 50, 75 oder 100 %**. Du schickst die abgerundete Zahl aus Truppen mal Anteil, mindestens 1. Bei 100 % schickst du „alles minus eins“, damit die Insel nie leer wird und dir gehört.

Eine Flotte fliegt geradlinig mit **2,5 Karteneinheiten pro Sekunde**. Eine Nachbarinsel in 4 bis 8 Einheiten Entfernung braucht etwa 1,6 bis 3,2 Sekunden, die ganze Karte zu überqueren dauert etwa 11 Sekunden. Flotten kämpfen nicht auf dem Meer; sie fliegen aneinander vorbei. Das hält die Ankunftsvorschau ehrlich, und die Spannung des Genres bleibt: Eine lange Reise ist ein Risiko, denn das Ziel wächst weiter, während du unterwegs bist.

## Eroberung, berechnet bei der Ankunft

- Kommst du bei einer eigenen Insel an, werden die Truppen addiert.
- Kommst du bei einer feindlichen oder neutralen Insel an, brauchst du mehr als **Verteidigung mal Multiplikator**. Der Multiplikator ist normalerweise 1,0 und **1,5 bei einer Festung**.
- Angriff über dem Bedarf: Du eroberst, und die neue Verteidigung ist der Rest. Gleich: Der Verteidiger hält mit 0 (bei Gleichstand gewinnt der Verteidiger). Darunter: Der Verteidiger verliert einen Teil.

Zwei Beispiele. Eine Flotte von 18 erreicht eine Festung mit 10. Der Bedarf ist ceil(10 × 1,5) = 15, du eroberst sie also mit 3 Rest. Eine Flotte von 12 bei derselben Festung lässt sie mit 2 zurück.

Kommen mehrere Flotten im selben Tick an, werden sie nacheinander in der Reihenfolge ihres Aufbruchs abgehandelt.

## Wie eine Partie endet

- **Sieg:** Der Gegner hat weder Inseln noch Flotten.
- **Klarer Sieg:** Hältst du 5 Sekunden lang das Dreifache der Gesamttruppen des Gegners und mindestens 60 % der Inseln, gibt der Gegner auf. Das erspart das langweilige Aufräumen einer ohnehin gewonnenen Partie.
- **Niederlage:** Du hast weder Inseln noch Flotten, oder du verlierst eine Insel, die du beschützen solltest.
- **Zeitlimit:** Nach 8 simulierten Minuten gewinnt der Spieler mit den meisten Inseln. Das sollte fast nie eintreten.

## Eine Engine für Echtzeit und Runden

Der Spielzustand hängt nur von der Startkarte, einem Seed und einer Liste von Befehlen ab, ohne Uhr und ohne Zufall in der Engine. Dieselbe Eingabe ergibt auf jedem Gerät dasselbe Ergebnis. Dadurch kann dieselbe Engine jetzt in Echtzeit und später in Netzwerkrunden laufen, und Wiederholungen sowie Fehlerberichte bestehen nur noch aus dem Speichern einer Befehlsliste.
