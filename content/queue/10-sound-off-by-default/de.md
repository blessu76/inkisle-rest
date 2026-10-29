---
title: Ton ist standardmäßig aus: eine Tonleiter für jedes Meer
description: Inkisle startet still, und der Spieler schaltet den Ton ein. Wie die Klänge im Code ohne Audiodateien entstehen, wie jedes Meer seine eigene Tonleiter mit fünf Tönen bekommt und warum eine Eroberungskette die Tonleiter hinaufsteigt.
slug: sound-off-by-default
lang: de
translation_of: en
category: making-of
keywords: Inkisle, Spielaudio, prozeduraler Sound, Pentatonik, Mobile Game, Barrierefreiheit, Einstellungen
image_alt: Fünf aufsteigende Töne, als kleine Tintenpunkte über einer Reihe von Inseln gezeichnet.
---
Viele Leute spielen am Telefon in der Öffentlichkeit oder im Bett. Ein Spiel, das laut startet, wird geschlossen. Deshalb ist in Inkisle **der Ton aus, bis der Spieler ihn einschaltet**, und diese Einstellung wird gespeichert.

## Aus heißt wirklich aus

Ist der Ton aus, wird der Audio-Code nicht einmal gestartet: Der Soundplayer wird erst erzeugt, wenn tatsächlich ein Ton gebraucht wird. Ein stummgeschaltetes Spiel berührt nie das Audiosystem des Telefons. Ist die gespeicherte Einstellung beschädigt oder schlägt der Speicher fehl, lautet die Antwort wieder „aus". Die App respektiert außerdem den Stumm-Schalter des Telefons. Fehler im Audio-Code werden abgefangen, statt nach außen zu dringen. Das war eine Korrektur, nachdem ein Code-Review gezeigt hatte, dass eine Art von Audiofehler durch das Sicherheitsnetz schlüpfen konnte.

## Keine Sounddateien

Jeder Klang wird **im Code erzeugt**. Die App baut für jeden Ton eine kurze 16-Bit-Mono-WAV mit 22.050 Samples pro Sekunde: eine Welle (Sinus, Dreieck oder Sägezahn), 12 ms Attack und ein exponentielles Ausklingen. Es gibt keine aufgenommenen Dateien, die lizenziert werden müssten. Die Tonparameter stammen aus dem Web-Prototyp, die App klingt also wie der Prototyp.

## Eine Tonleiter für jedes Meer

Jedes Meer hat seine eigene **Pentatonik**, fünf Töne, die in jeder Reihenfolge gut klingen:

| Meer | Schritte über dem Grundton (Halbtöne) |
|---|---|
| Ruhige Bucht (Calm Bay) | 0, 2, 4, 7, 9 |
| Windstraße (Windy Strait) | 0, 2, 5, 7, 9 |

Der Grundton beträgt 523,25 Hz. Das zweite Meer unterscheidet sich in einem Ton, dem dritten Schritt (5 statt 4).

## Ketten steigen

Wenn du mehrere Inseln hintereinander erobert, liegt **jede Eroberung einen Schritt höher** in der Tonleiter des Meeres. Nach fünf Schritten springt die Tonleiter eine Oktave höher, und oberhalb des zehnten Schritts bleibt sie auf dem höchsten Ton. Eine gute Kette ist daher als aufsteigende Linie hörbar, und weil die Tonleiter nur zusammenpassende Töne enthält, bleibt auch eine schnelle Kette sauber gestimmt.

## Was wir nicht geprüft haben

- Die Tests prüfen die Töne und dass stumm auch still bedeutet. Sie können uns nicht sagen, ob es **angenehm klingt**. Außerhalb des Teams hat niemand es über den Lautsprecher eines echten Telefons oder mit Kopfhörern gehört.
- Diese Töne sind schlichte Pieptöne. Ob sie als endgültiger Klang bleiben oder ersetzt werden, ist nicht entschieden.
