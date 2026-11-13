---
title: Zwei Tinten-Items gleichzeitig: Slots, Abstände und was uns die Bots verraten haben
description: In den frühen Meeren konnte man nur ein Tinten-Item auf einmal nutzen. Ab Meer 5 sind es zwei, später drei, mit einem Abstand zwischen den Starts. Die Regeltabelle, wie der Button sie zeigt, und eine Simulation, die einen viel kleineren Effekt fand, als wir erwartet hatten.
slug: two-inks-at-once
lang: de
translation_of: en
category: making-of
keywords: Inkisle, Tinten-Items, Spieldesign, Spielbalance, Bot-Simulation, mobile Oberfläche, Barrierefreiheit
image_alt: Zwei kleine Tintentropfen nebeneinander über einer Reihe von Inseln, in weichen Vektorfarben gezeichnet.
published: 2026-11-13T22:44+09:00
---
Tinten-Items (Schub, Anker, Nebel, Laterne, Gezeitenwechsel) liefen bisher immer nur eines nach dem anderen. Das ist leicht zu verstehen, bedeutet aber auch, dass sich ein späterer Level nie so anfühlt, als hätte man mehr Werkzeuge. Deshalb haben wir dem Tinten-Button **Slots** gegeben.

## Die Regel

| Meer | Slots gleichzeitig | Abstand zwischen Starts |
|---|---|---|
| 1 bis 4 | 1 | keiner (wie bisher) |
| 5 bis 10 | 2 | 10 Sekunden |
| Band 2, Meere 11 bis 20 | 2 | 5 Sekunden |
| Band 3, ab Meer 21 | 3 | 5 Sekunden |

Was gleich geblieben ist: Ein Boss fügt dem Abstand 5 Sekunden hinzu, das Limit an Einsätzen pro Level (5 oder 6) gilt für alle Slots gemeinsam, man kann nicht zwei Items derselben Art gleichzeitig nutzen, ein Anker- oder Nebel-Slot wird frei, sobald seine Insel erobert ist, und die ersten 20 Sekunden eines Levels sperren weiterhin jede Tinte.

## Wie der Button es zeigt

Der Tinten-Button hat einen Punkt pro Slot, der gefüllt ist, solange der Slot läuft. Ein dünner Ring im Button zählt den Abstand herunter, bevor man das nächste starten darf. Im Hafenblatt steht auf einer gesperrten Karte „nächste Tinte in N Sekunden“ für den Abstand oder „breitet sich aus“, wenn die Slots voll sind. Das Bedienungshilfen-Label lautet etwa „1 von 2 Slots“. All das gibt es in 12 Sprachen.

## Warum die Engine keinen neuen Hash brauchte

Der Spielzustand enthält bereits eine Liste der Endzeiten laufender Tinte und die Anzahl der Einsätze, sodass sich die Meere 1 bis 4 genau wie zuvor verhalten und denselben Hash ergeben. Die Tests decken jede Zeile der Tabelle ab, das Verhalten im ersten Meer, die Ablehnung derselben Art, volle Slots, drei Slots, das gemeinsame Limit und die Freigabe bei Eroberung sowie den Button bei 320 und 375 px.

## Was die Bots sagten

Wir haben 80 Level von Meer 5 bis 14 simuliert, fünf Bots mit je 24 Seeds, für vier Pläne mit zwei oder drei Items, die bei 20 Sekunden beginnen, und den besten Plan unter der alten Regel (ein Slot, kein Abstand) mit der neuen Regel verglichen.

- Der durchschnittliche Gewinn lag bei **+1,1 Prozentpunkten** (+0,9 in den Meeren 5 bis 10, +1,5 in den Meeren 11 bis 14). Wir hatten 3 bis 8 erwartet.
- Bei Bossen waren es +0,9. Die beste Siegquote mit Tinte gegenüber keiner Tinte lag bei +36 Punkten, innerhalb unserer Grenze von 40.
- Level für Level schwankte die Veränderung zwischen −7 und +10, was etwa dem Rauschen von 24 Seeds entspricht.

Die Bots nutzen den zweiten Slot selten gut, deshalb sagt die kleine Zahl vielleicht mehr über die Bots als über die Regel. **[nicht verifiziert]** Ein Mensch könnte mehr gewinnen.

## Was wir nicht geprüft haben

- Ob ein Mensch zwei Slots und einen Abstand klar findet oder ob es sich wie eine Sperre anfühlt. Wir haben es nicht auf einem echten Handy getestet. **[nicht verifiziert]**
- Ein einzeiliger Hinweis, wenn man zum ersten Mal ein Meer mit zwei Slots erreicht (5-1), ist noch nicht gebaut.
- Das Spiel ist in Entwicklung und nicht veröffentlicht.
