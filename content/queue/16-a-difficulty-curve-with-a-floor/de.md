---
title: Eine Schwierigkeitskurve mit Boden: keine Stufe, die der einfachste Bot nie gewinnen kann
description: Bei Hunderten von Stufen sind ein paar schwere Stufen nicht einfach ein paar schwere Stufen, sondern eine Mauer. Wir haben alle 14 Meere auf eine Kurve mit einer Ruhestufe in jedem Meer umgestellt, die Stärke der Gegner-KI begrenzt und einen Test ergänzt, der fehlschlägt, wenn der einfachste Bot 0 von 40 gewinnt. Das Vorher und Nachher.
slug: a-difficulty-curve-with-a-floor
lang: de
translation_of: en
category: making-of
keywords: Inkisle, Schwierigkeitskurve, Spielbalance, Bot-Simulation, Leveldesign, Siegquote, KI-Stufe
image_alt: Eine gewundene Reihe von Inseln, die wie eine Welle steigt und fällt, gezeichnet in sanften Vektorfarben.
---
Ein Kommentar des Inhabers hat diese Arbeit verändert: Wenn nur 40 von 800 Stufen gewinnbar sind, ist das Spiel zu schwer, auch wenn jede Stufe für sich in Ordnung aussieht. Also haben wir aufgehört, Stufen einzeln abzustimmen, und eine **Kurve** aufgeschrieben.

## Die Kurve

- Jedes Meer hat acht Stufen mit einer **Rolle**: Auftakt, Aufbau, eine Ruhestufe, Anstieg, Boss. Die Ruhestufe soll leicht sein; der einfachste Bot gewinnt sie mindestens zu 80 % der Zeit.
- Die angestrebte Siegquote folgt außerdem einer **Welle über die Bände hinweg**: Ein Meer ist ein wenig schwerer als das vorherige, dann kommt wieder ein sanfteres Meer.
- Die Meere 1 bis 3 sind schon in TestFlight-Builds, deshalb haben wir ihre leichten Werte in Ruhe gelassen.

## Eine Obergrenze für den Gegner

Manche Stufen waren schwer, weil die Gegner-KI zu clever war, nicht weil die Karte hart war. Wir haben eine **KI-Obergrenze** eingeführt: Stufe 5 nur für Stufen mit mehreren Gegnern, Stufe 4 für Meer 11 und höher sowie für Bosse und die siebte Stufe ab Meer 6, Stufe 3 überall sonst. Jede KI über ihrer Obergrenze wird beim Laden der Stufe herabgesetzt. Ein Beispiel: In 10-8 ging der Admiral von Stufe 5 auf 3, und die Verteidigung des neutralen Leuchtturms von 10 auf 5.

## Die Messung

Alle 14 Meere, fünf Bots, je 40 Seeds. Der „einfache Bot“ ist der schwächste der fünf und steht stellvertretend für einen Menschen.

| | Vorher | Nachher |
|---|---|---|
| Stufen, die der einfache Bot nie gewinnt | **9** (3-8, 4-3, 4-6, 5-5, 6-8, 7-6, 10-3, 10-8, 14-2) | **0** |
| Schwächste Stufe | 0 Siege aus 40 | 4 Siege aus 40 (8-8), dann 5 aus 40 (10-8) |
| Ruhestufen, einfacher Bot | nicht erfasst | mindestens 80 % |

Einige Beispiele für die Siege des einfachen Bots aus 40: 3-8: 0 → 30. 4-3: 0 → 18. 6-1: 2 → 39. 7-6: 0 → 17.

## Ein Test, der den Boden hält

`curve_floor_test` schlägt fehl, wenn der einfache Bot irgendwo 0 von 40 gewinnt, wenn eine Ruhestufe unter 80 % fällt oder wenn der Durchschnitt der fünf Bots zu weit vom Kurvenziel abweicht. Die Zielwerte stehen in einer einzigen Datei, die Kurve zu ändern heißt also, eine Tabelle zu ändern.

## Was wir absichtlich leichter gemacht haben, und der Preis

Die leichteren Stufen haben die **Tinte**-Gegenstände wertvoller gemacht, denn eine Stufe, die leichter zu gewinnen ist, profitiert auch stärker von einem Bonus. Um die gewünschten Stufen zu behalten, haben wir zwei Tinten-Schranken gelockert: Die Obergrenze für die Siegquote eines Bosses mit Tinte stieg in fünf Boss-Stufen von 55 % auf 75 %, und der Gewinn durch eine Tintenverwendung stieg in vier Stufen von 25 auf 35 Prozentpunkte. Das sind Ausnahmen, die wir festgehalten haben, und es muss noch entschieden werden, wie viel Tinte wert sein soll. **[als Richtlinie nicht verifiziert]**

## Was wir nicht geprüft haben

- Die Siegquoten stammen von Bots. Einige Stufen (4-6, 5-7, 9-5, 10-2, 10-3, 11-6) liegen etwa zehn Punkte neben dem Ziel, und 10-8 hat einen Bot-Durchschnitt von 62 % bei einem Ziel von 33 %, weil der Admiral für den einfachsten Bot sehr schwer, für die anderen aber leicht ist.
- Niemand hat die neue Kurve von Hand gespielt; „40 von 800 ist zu schwer“ ist also nur in den Zahlen der Bots behoben. **[nicht verifiziert]**
- Das Spiel ist in Entwicklung und nicht veröffentlicht.
