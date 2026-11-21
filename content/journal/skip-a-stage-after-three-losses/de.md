---
title: Level nach drei Niederlagen überspringen: ein sanftes Angebot mit Preis
description: In Inkisle fragt das Spiel nach drei Niederlagen im selben Level, ob man es für 3 Ink überspringen will. Wann es fragt, welche Level ausgenommen sind, wie das Seekartenzeichen aussieht und wie es gespeichert wird.
slug: skip-a-stage-after-three-losses
lang: de
translation_of: en
category: making-of
keywords: Inkisle, Level überspringen, Schwierigkeit, Spieldesign, Speicherdaten, Mobile Game
image_alt: Eine Seekarte mit einer Insel, die eine kleine korallenrote Flagge trägt, und einem gepunkteten Weg an ihr vorbei zur nächsten Insel.
published: 2026-11-21T12:30+09:00
---

In Inkisle, unserem Insel-Eroberungsspiel für iOS, erscheint nach drei Niederlagen im selben Level die Frage: „Dieses Level überspringen und später versuchen?“ Das Überspringen kostet 3 Ink. Das übersprungene Level bekommt auf der Seekarte eine Flagge und lässt sich jederzeit spielen. Das Spiel ist noch in Entwicklung und nicht veröffentlicht; das Popup haben wir noch nicht auf einem echten Gerät gesehen.

## Warum überhaupt überspringen

Auch nach der Feinabstimmung bleiben einige Level besonders schwer. Wir wollten nicht, dass jemand an einer Insel hängen bleibt. Das Angebot lässt Spielende weiterziehen und zurückkehren, statt aufzuhören.

## Wann es fragt

- Direkt nach der **dritten Niederlage** im selben Level, sobald sich das Ergebnisblatt gesetzt hat (1,1 Sekunden).
- Bei Ablehnung fragt es bei der 4. und 5. Niederlage nicht, aber bei der **6., 9.** und so weiter. Jedes Mal zu fragen wäre lästig; nur einmal zu fragen würde jemanden übersehen, der weiter festhängt.
- Niederlagen zählen pro Level. Ein Sieg setzt den Zähler auf 0. Niederlagen in bereits geschafften oder übersprungenen Leveln zählen nicht.

## Was es kostet

Das Überspringen kostet **3 Ink**, dasselbe Ink, das man im Spiel verdient oder kauft. Es gibt keine neue Währung und kein neues Produkt. Der Wert ist eine einzige Konstante im Code; Popup-Text, Schaltfläche und Link zum Shop richten sich danach.

Zuerst war es 1 Ink; nach dem Wunsch des Besitzers nach 2 bis 3 wurden es 3. Bei weniger als 3 Ink wird die Schaltfläche zu „Kein Ink, Shop öffnen“ und öffnet das bestehende Shop-Blatt. Ab 3 Ink kehrt die Überspringen-Schaltfläche zurück.

## Welche Level ausgenommen sind

- 1-1 bis 1-4: der Tutorial-Abschnitt ohne Ink. Wer dort überspringt, lernt die Steuerung nie.
- 1-5: das Level, in dem das Spiel das erste Ink schenkt.
- Das letzte Level: Es gibt kein nächstes, das sich öffnen ließe.
- Boss-Level sind eingeschlossen.

## Was ein übersprungenes Level bedeutet

- Das nächste Level öffnet sich, das übersprungene hat **0 Sterne**. Überspringen ist kein Sieg, Sterne lassen sich nicht kaufen.
- Auf der Seekarte bekommt der Knoten eine korallenrote Flagge; Screenreader ergänzen „übersprungen“.
- Wird es später geschafft, verschwindet die Flagge und die Sterne werden normal gespeichert.
- Ein Meer gilt nur mit geschafften Leveln als abgeschlossen, das geflaggte Level muss also selbst gewonnen werden.
- Das Ende öffnet sich nur bei einem echten Sieg; 10-8 zu überspringen öffnet es nicht.

## Wie es gespeichert wird

Der bestehende Fortschrittseintrag bekommt zwei optionale Schlüssel: die Fehlversuche pro Level und die Liste übersprungener Level. Sind beide leer, werden sie nicht geschrieben, ein alter Spielstand bleibt Byte für Byte gleich. Beim Lesen werden unbekannte IDs sowie negative Werte und Texte verworfen, und bei bereits geschafften Leveln wird die Überspringen-Markierung entfernt, denn der Sieg zählt mehr.

Beim iCloud-Abgleich gilt die größere Fehlerzahl, übersprungene Listen werden vereinigt, und ein Sieg auf einem anderen Gerät hat Vorrang. Denselben Snapshot erneut abzugleichen ändert nichts; ein Test prüft das.

## Was wir nicht geprüft haben

- Popup und Flagge auf einem echten Gerät oder Simulator. Widget-Tests mit 375 und 320 Breite fanden in 16 Sprachspalten keinen Überlauf, Screenshots haben wir aber nicht angesehen.
- Ob eine ältere App-Version, die den iCloud-Snapshot überschreibt, die beiden neuen Schlüssel verliert. Dann blieben geschaffte Level und Sterne erhalten, nur die Markierung ginge nach unserer Einschätzung verloren.
- Übersetzungen außer Koreanisch und Englisch wurden nicht von Muttersprachlern geprüft.

## Häufige Fragen

### Wann bietet Inkisle das Überspringen an?

Nach drei Niederlagen im selben Level, bei weiterem Versuchen erneut nach der 6., 9. und so weiter. Der erste Abschnitt, das Geschenk-Level 1-5 und das letzte Level sind ausgenommen.

### Was kostet es, und bekomme ich Sterne?

Es kostet 3 Ink. Ein übersprungenes Level gibt 0 Sterne; wer es später schafft, bekommt sie wie gewohnt.

### Schließt Überspringen ein Meer ab oder öffnet es das Ende?

Nein. Ein Meer ist nur mit geschafften Leveln abgeschlossen, und das Ende öffnet sich nur bei einem echten Sieg.
