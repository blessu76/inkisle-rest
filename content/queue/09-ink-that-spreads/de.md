---
title: Tinte, die sich ausbreitet: die kleinen Effekte, die sagen, was gerade passiert ist
description: In Inkisle hinterlässt eine eroberte Insel einen Tintenklecks, ein Comeback zeigt ein Banner, und die letzte feindliche Insel leuchtet auf. Wozu jeder Effekt dient, wie lange er dauert und wie der Fingerhinweis beim ersten Start funktioniert.
slug: ink-that-spreads
lang: de
translation_of: en
category: making-of
keywords: Inkisle, Spielgefühl, visuelles Feedback, Mobile Game, Einsteigerhinweis, Animation
image_alt: Ein korallenfarbener Tintenklecks breitet sich über eine eroberte Insel aus, während Flotten zwischen anderen Inseln unterwegs sind.
---
In einem Spiel, in dem man die Karte in die eigene Farbe taucht, ist der wichtigste Moment, wenn **eine Insel den Besitzer wechselt**. Ist es nur ein Farbwechsel, übersieht man ihn auf einem kleinen Bildschirm leicht. Deshalb haben wir ein paar kleine Effekte hinzugefügt, deren Aufgabe es ist, „das ist gerade passiert" zu sagen.

## Der Eroberungsklecks

Wenn eine Insel den Besitzer wechselt, breitet sich von ihr ein **Tintenklecks** in der Farbe des neuen Besitzers aus und blendet aus. Er dauert etwa **0,75 Sekunden**. Die Form ist ein unregelmäßiger Fleck, der genauso gezeichnet wird wie die Kleckse im Intro, sodass Spiel und Eröffnung verwandt wirken. Ein Test prüft, dass eine Eroberung einen Klecks hinterlässt und dieser danach verschwindet.

## Drei Momente mit einer Meldung

- **Ein Comeback.** Wenn du zurücklagst und die Führung übernimmst, erscheint **einmal** ein Banner. Es wird etwa 1,6 Sekunden gezeigt. „Einmal" ist wichtig: Ein Banner, das bei jedem Führungswechsel hin und her aufblitzt, wird zu Lärm.
- **Die letzte Insel.** Wenn dem Gegner nur noch **seine letzte Insel** bleibt, wird diese hervorgehoben, damit du weißt, wohin du zielen musst.
- **Ein Meer abschließen.** Ein ganzes Meer zu räumen hat einen eigenen kurzen Moment, getrennt vom Ergebnisblatt einer einzelnen Stufe.

## Der Fingerhinweis beim ersten Start

Ein neuer Spieler weiß nicht, dass man von einer Insel zur anderen zieht. Beim ersten Mal in einer Stufe **streicht ein kleiner Finger von deiner Insel zur nächsten anderen Insel**. Er verschwindet, sobald du irgendetwas losschickst, und ein Test prüft das. Wir haben ihn klein und kurz gehalten, damit ein Spieler, der die Steuerung schon kennt, nicht ausgebremst wird.

## Was wir nicht geprüft haben

- All das ist durch Tests abgedeckt, **wann** ein Effekt erscheint, nicht **wie er sich anfühlt**. Timing, Größe und Farbe sind erste Vermutungen und wurden außerhalb des Teams von niemandem auf einem echten Telefon ausprobiert.
- Wir wissen noch nicht, ob das Comeback-Banner ermutigend ist oder nur ablenkt.
