---
title: Eine Seekarte, die ihren Weg wechselt: ein Linienstil pro Meer
description: Bei 14 Meeren auf einer scrollenden Karte sah der Weg zwischen den Stufen überall gleich aus. Wir haben jedem Meer einen eigenen Linienstil, eine eigene Farbe und eine eigene Schlängelung gegeben, den Winkel über Meergrenzen hinweg fortgeführt und zeichnen nur, was auf dem Bildschirm ist. Die Werte, die Tests und was wir noch nicht auf einem Handy gesehen haben.
slug: a-chart-that-changes-its-road
lang: de
translation_of: en
category: making-of
keywords: Inkisle, Seekarte, Levelkarte, Routenstil, Mobile UI, Flutter, Rendering-Performance
image_alt: Ein gewundener gepunkteter Weg zwischen Inseln, der von einer Seillinie in eine Wellenlinie übergeht, gezeichnet in weichen Vektorfarben.
published: 2026-11-12T19:00+09:00
---
Die Karte ist der Bildschirm, auf dem du die ruhige Zeit zwischen den Kämpfen verbringst: ein langer Weg aus Stufen. Bei 14 Meeren sah der Weg die ganze Strecke gleich aus. Ein langes Scrollen ohne Veränderung wirkt wie ein einziges, wiederholtes Meer. Deshalb hat jedes Meer seinen eigenen Weg bekommen.

## Was sich pro Meer ändert

| Meer | Linie | Farbe eines abgeschlossenen Wegs |
|---|---|---|
| 1 | durchgezogen (wie zuvor) | Koralle |
| 2 | Seil | Segelbeige |
| 3 | lange Striche, blass | Leuchtturmweiß |
| 4 | Welle | Petrol |
| 5 | Perlen | Korallrosa |
| 6 | lange Striche | Sandgold |
| 7 | dick durchgezogen | Marineblau |
| 8 | dünn durchgezogen | Kobalt |
| 9 | Perlen | Laternengold |
| 10 | dick durchgezogen | Gold |
| 11 | Pinsel | Tinte |
| 12 | Doppellinie | Silber |
| 13 | Welle | weißes Segel |
| 14 | Perlen | tiefe Tinte |

Jedes Meer hat außerdem sein eigenes Schwingen (wie weit der Weg zur Seite ausschlägt und wie oft). Sieben Linientypen werden von den 14 Meeren gemeinsam genutzt, und die Farben sind alle verschieden. Der Weg zu einer Stufe wird im Stil des Meeres gezeichnet, zu dem die Stufe gehört. Nach Meer 14 wiederholen sich die Stile, vorläufig.

## Zwei Dinge, bei denen es nicht ums Aussehen ging

- **Kein Sprung an den Meergrenzen.** Das Schwingen ist eine einzige stetige Funktion, daher setzt sich der Winkel dort fort, wo ein Meer endet und das nächste beginnt, und die Inseln springen nicht zur Seite.
- **Nur Sichtbares zeichnen.** Die Karte wird Hunderte von Stufen haben, deshalb werden Inseln und Wege außerhalb des sichtbaren Bereichs übersprungen. In einem Widget-Test dauerte das Zeichnen von zehn sichtbaren Wegen weniger als 16 ms.

## Die Verzierungen kamen danach

In einem zweiten Schritt kamen kleine Markierungen entlang des Wegs pro Meer hinzu: Knoten, Klammern, Fußspuren, Sterne, Tintentropfen. In den Meeren 7, 10 und 11 haben wir sie dann in einen Wirbel, ein Leuchtfeuer und eine Ausbreitung geändert, und den Tropfen von Meer 14 in einen spitzen.

## Tests

Sieben Tests prüfen, dass jedes Meer einen Stil hat, dass das Schwingen unter .32 bleibt, dass die 14 Farben alle verschieden sind, dass jeder Linientyp verwendet wird, dass ein abgeschlossener Weg einen Kontrast von mindestens 3:1 zu seinem Rand hat, dass die Inseln bei 320 px innerhalb von 18% bis 82% der Breite bleiben und dass jedes Meer andere Pixel zeichnet. Das Layout des ersten Meeres bewegt sich nicht.

## Was wir nicht geprüft haben

- Alle bisherigen Darstellungen sind Test-Aufnahmen, in denen die Schrift ein Block ist. Wir haben es nicht auf einem echten iPhone oder Android-Handy angesehen. **[nicht verifiziert]**
- Wir haben die Frame-Zeit nicht mit allen 800 Stufen gemessen, nur die Prüfung mit zehn Wegen. **[nicht verifiziert]**
- Auf den dunklen Nachtmeeren (11 und 14) wird der tintenfarbene Weg von einem weißen Rand getragen. Ob das richtig aussieht, ist eine Design-Prüfung, die wir noch schuldig sind.
- Das Spiel ist in Entwicklung und nicht veröffentlicht.
