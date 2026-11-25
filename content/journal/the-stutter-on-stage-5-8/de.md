---
title: Das Ruckeln in Level 5-8: Es lag am Bildschirm, nicht an der Spiel-Engine
description: Level 5-8 in Inkisle ruckelte. Wir haben gemessen, bevor wir etwas angefasst haben, und festgestellt, dass die Kosten im Zeichnen des Bildschirms lagen und nicht in den Spielregeln. Auf einem Computer sank der Aufwand pro Frame von 3,4 auf 1,3 ms. Was wir geändert haben, was wir belassen haben und was wir auf einem Handy noch nicht geprüft haben.
slug: the-stutter-on-stage-5-8
lang: de
translation_of: en
category: making-of
keywords: Inkisle, Leistung, Ruckeln, Frame-Zeit, Spieldesign, Mobilspiel, Optimierung
image_alt: Links vier hohe violette Balken, rechts vier niedrige korallenrote Balken, dazwischen ein Pfeil und eine gestrichelte Linie, die das Budget markiert.
published: 2026-11-25T15:15+09:00
---

Inkisle, unser Inseleroberungs-Strategiespiel für iOS, ruckelte beim Testen in Level 5-8. Die naheliegende Vermutung war, dass die Spiel-Engine, die Flotten bewegt und Eroberungen entscheidet, zu schwer geworden war. Wir haben zuerst gemessen. Das Problem war nicht die Engine, sondern der Bildschirm um sie herum. Nach der Änderung sank der Aufwand eines Frames in Level 5-8 auf unserem Computer von 3,4 ms auf 1,3 ms. Das Spiel ist in Entwicklung und nicht veröffentlicht, und diese Zahlen stammen nicht von einem Handy.

## Was wir gemessen haben

Ein Frame enthält zwei Arten von Arbeit: die Spielregeln um einen Tick voranbringen und den Bildschirm aufbauen und zeichnen. In Level 5-8 kostete ein Tick der Regeln im Mittel nur 3 bis 5 Mikrosekunden. Der Bildschirm kostete etwa tausendmal mehr.

Der größte Teil dieser Bildschirmkosten kam von drei Dingen:

1. **Das gesamte Heads-up-Display wurde in jedem Frame neu aufgebaut.** Der Spiel-Controller meldete in jedem Frame eine Änderung, sodass Kraftbalken, Zieltext, Ergebnisblatt, Verhältnisbalken, Abzeichen, Auswahlleiste, Krisen-Overlay und Gezeitenknopf alle neu gebaut wurden, auch wenn sich nichts geändert hatte. Etwa 2,5 ms der 3,4 ms gingen in den Aufbau von Widgets.
2. **Zahlenbeschriftungen verfehlten den Cache.** Der Cache-Schlüssel enthielt die genaue Transparenz und Größe jeder Zahl, und diese ändern sich bei einer Eroberungswelle oder einer Ausblendung fortlaufend. So entstanden in jedem Frame neue Layouts, und wenn der Cache 600 Einträge überschritt, wurde er ganz geleert, sodass ein Frame alles neu setzen musste. Die Zeichenzeit im langsamsten 1 Prozent der Frames war das 5- bis 10-Fache des Mittelwerts.
3. **Kleine wiederholte Arbeit.** Jede Flotte schlug ihre Tintenfarbe zweimal nach, Position und Radius jeder Insel wurden für jede Flotte neu berechnet, und ein Shader-Cache verwendete einen Textschlüssel.

## Was wir geändert haben

- Das Heads-up-Display hört jetzt auf ein kleines Signal, das nur ausgelöst wird, wenn sich etwas ändert, das es anzeigt, etwa Tick, Pause, Geschwindigkeit, Krisenzustand, Ziele oder Hinweise. Das Zeichnen geschieht wie bisher in jedem Frame.
- Zahlenbeschriftungen werden auf grobe Stufen gerundet (Transparenz in 32 Stufen, Größe in Viertelpixeln), damit der Cache trifft; wenn er voll ist, wird nur die ältere Hälfte entfernt.
- Wiederholte Nachschlagevorgänge werden einmal pro Frame berechnet, und der Shader-Schlüssel wurde von einem String zu einem Record.

Die Rundung von Größe und Transparenz ist mit dem Auge nicht zu sehen.

## Die Zahlen

Sie wurden auf einem Computer bei einem 375 × 667 großen Bildschirm gemessen, in einem Modus, der nur zum Vergleich von vorher und nachher taugt.

| | vorher | nachher |
|---|---|---|
| Level 5-8, ganzer Frame, Mittelwert | 3.433 µs | 1.267 µs |
| Level 5-8, ganzer Frame, langsamstes 1 % | 10.803 µs | 5.182 µs |
| Level 5-8, Zeichnen, Mittelwert | 818 µs | 201 µs |
| Level 5-8, Zeichnen, langsamstes 1 % | 4.540 µs | 1.284 µs |

Ein Spiel mit 60 Bildern pro Sekunde hat etwa 16,6 ms pro Frame, daher passte die Arbeit schon vor der Änderung auf einem Computer in dieses Budget. Deshalb kann das Ruckeln, das wir gespürt haben, auch eine andere Ursache haben (siehe unten).

## Was wir belassen haben

Wir haben keine einzige Zeile der Regeln oder des Balance-Codes verändert. Nur die Bildschirmschicht hat sich geändert: wie der Controller Aktualisierungen meldet, welche Widgets zuhören und die Zeichen-Caches. Derselbe Seed liefert weiterhin dasselbe 600-Tick-Ergebnis, und die bestehenden Prüfungen für Referenzbilder, deterministisches Spielen und Bot-Simulationen blieben grün.

Eine echte Kostenstelle haben wir für später aufgehoben. Die Krisenprognose läuft im Bildschirm-Thread: im schwersten Level, das wir gemessen haben, 17-3, brauchte sie im Mittel 3,4 ms, und ihr langsamstes 1 Prozent erreichte 11,8 ms, was alle halbe Sekunde einen kleinen Hänger verursachen kann. Diese Arbeit auf mehrere Frames zu verteilen würde dasselbe Ergebnis liefern, riskiert aber veränderte Entscheidungen, deshalb haben wir es jetzt nicht getan. In Level 5-8 kostet sie 0,17 ms und spielt keine Rolle.

## Was wir hinzugefügt haben

Einen Benchmark für die Engine ohne Bildschirm und einen Leistungstest mit lockeren Obergrenzen. Er fängt die Art von Rückschritt ab, bei der die Kosten mit der Flottenzahl explodieren oder jeder Frame zu viel Speicher belegt. Wir haben die Grenzen mit Absicht locker gehalten, weil enge Grenzen immer dann scheitern würden, wenn der Testrechner beschäftigt ist. Standardmäßig werden die schwersten dieser Tests übersprungen und laufen nur auf Anforderung.

## Was wir nicht geprüft haben

- **Die Bildrate auf einem echten Handy, bei 60 oder 120 Bildern pro Sekunde, ist ungeprüft.** Unsere Zahlen sind Kosten des Bildschirm-Threads auf einem Computer, keine Grafikkosten auf einem Gerät.
- **Der Nebelschleier und die Bandebenen sind weder gemessen noch geändert.** Sie werden mit einer Vollbild-Unschärfe gezeichnet, die den Grafikchip und nicht den Prozessor belastet. Ruckelt Level 5-8 auf einem Handy weiterhin, ist das unser erster Verdächtiger.
- Wir haben die Browser-Darstellung bei 320, 375, 768 und 1280 px nicht angesehen, weil sich kein Layout geändert hat.
- Dass sich die Eingabe reaktionsfreudiger anfühlt, ist nur unsere Erwartung.

## FAQ

### Warum ruckelte Level 5-8 in Inkisle?

Unsere Messung wies auf den Bildschirm hin, der in jedem Frame neu aufgebaut wurde, und auf Zahlenbeschriftungen, die jedes Mal neu gesetzt wurden, nicht auf die Spielregeln. Das haben wir behoben; die Bildrate auf einem echten Handy ist noch nicht geprüft.

### Hat die Optimierung verändert, wie das Spiel gespielt wird?

Nein. Wir haben die Regeln und den Balance-Code nicht angefasst, und derselbe Seed liefert dasselbe Ergebnis wie zuvor.

### Ruckelt es auf einem Handy noch?

Das wissen wir noch nicht. Unsere Zahlen stammen von einem Computer. Wir prüfen es auf einem echten Gerät in TestFlight.
