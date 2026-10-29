---
title: Drei Sterne, eine Regel: wie ein Level bewertet wird
description: Jedes Level in Inkisle kann bis zu drei Sterne einbringen. Was jeder Stern bedeutet, warum Sterne den Fortschritt nie blockieren und nie sinken, die 13 Arten von Drei-Sterne-Zielen und die falsche Beschriftung, die wir gefunden und behoben haben.
slug: three-stars-one-rule
lang: de
translation_of: en
category: making-of
keywords: Inkisle, Sternebewertung, Spielfortschritt, Spieldesign, Mobile Game, Wiederspielwert
image_alt: Eine Reihe aus drei Sternen, die ersten beiden korallenrot gefüllt, der dritte nur als Umriss.
---
Jedes der 16 Level in Inkisle gibt einen bis drei Sterne. Sterne sind die Art des Spiels zu sagen „du kannst es besser“, ohne dich dazu zu zwingen. Hier die Regel und ein Fehler, den wir beim Erklären gemacht haben.

## Was jeder Stern bedeutet

1. **★1: gewinnen.** Du schlägst das Level.
2. **★2: innerhalb des Zeitlimits des Levels gewinnen.** Jedes Level hat sein eigenes Limit.
3. **★3: das eigene Ziel des Levels.** Ein anderes Ziel für jedes Level, angezeigt auf seiner Karte.

Das Spiel entscheidet diese drei Bedingungen an einer einzigen Stelle, und die Bildschirme fragen nur nach dem Ergebnis. Das klingt selbstverständlich, aber als wir zuerst die Übersicht und das Ergebnisblatt schrieben, waren Teile der Regel in beide hineingesickert. Ein Review fand das, und wir verlegten die Prüfungen in kleine Hilfsfunktionen neben der Regel, sodass es bei einer Änderung der Regel nur eine Stelle zu ändern gibt.

## Sterne stehen nie im Weg

- **Sterne schalten nichts frei.** Ein gewonnenes Level öffnet das nächste. Den Boss zu besiegen öffnet das nächste Meer.
- **Sterne sinken nie.** Spielst du ein Level erneut und verlierst, wird nichts gespeichert. Spielst du erneut und gewinnst, behält das Spiel von allem das Beste: Ein einmal verdienter Stern bleibt, und die beste Zeit wird behalten.

Ein erneutes Spielen kann dir also nur helfen.

## Dreizehn Arten von Drei-Sterne-Zielen

Das ★3-Ziel ist in fast jedem Level anders. Bisher gibt es 13 Arten, zum Beispiel:

- höchstens eine bestimmte Zahl an Truppen verlieren,
- gewinnen, ohne je 100 % zu senden,
- jede leere Insel einnehmen,
- keine einzige Insel verlieren,
- eine Festung mit einem Angriff erobern,
- einen gleichzeitigen Angriff des Gegners einmal abwehren,
- die Heimatinsel des Gegners nicht vor einer bestimmten Zeit angreifen.

Jedes Ziel steht in der App in einfachen Worten, zum Beispiel „Gewinne, ohne 100 % zu senden.“

## Die falsche Beschriftung

Die Beschriftung von ★1 lautete zuerst „**gewinnen und dabei deine Inseln behalten**“. Die Bedingung war aber nur „gewinnen“: Du konntest Inseln verlieren und trotzdem den Stern bekommen. Die Beschriftung versprach etwas, das das Spiel nicht prüfte. Ein Review fing das ab, und die Beschriftung lautet jetzt einfach „**gewinnen**“.

## Was wir nicht überprüft haben

- Die Zeitlimits für ★2 wurden vom Prototyp festgelegt und wirken, wie der Bot-Test in einem früheren Beitrag zeigte, für Bots **zu großzügig**. Wir wissen noch nicht, wie menschliche Zeiten aussehen.
- Wir wissen nicht, ob Spielerinnen und Spieler 13 verschiedene Ziele interessant oder nur verwirrend finden.
