---
title: Die Tintenquelle des Weißen Meeres: wenn sich eine Drei-Sterne-Regel nicht erreichen lässt
description: Meer 14 hat eine Quelle, die Tinte auf nahe Inseln ausbreitet. Bots konnten das Drei-Sterne-Ziel "lass die Quelle sich auf N Inseln ausbreiten" nicht erreichen, also haben wir gemessen, Inseln verschoben und die Regel durch eine Zählung der Quellenpulse ersetzt. Was wir versucht haben und was noch ungeprüft ist.
slug: the-white-sea-ink-spring
lang: de
translation_of: en
category: making-of
keywords: Inkisle, Leveldesign, Drei-Sterne-Regel, Tintenquelle, Bot-Simulation, Spielbalance, Meer 14
image_alt: Ein helles Meer mit einer kleinen Quelleninsel in der Mitte und ein paar Inseln ringsum, gezeichnet in weichen Vektorfarben.
published: 2026-11-10T19:00+09:00
---
Meer 14, das Weiße Meer, bringt eine Regel dazu: eine **Tintenquelle**. Hältst du die Quelleninsel, pulsiert sie alle 150 Ticks und breitet Tinte auf eine nahe Insel aus. Der erste Puls kommt 150 Ticks nach der Eroberung. Das Drei-Sterne-Ziel, das wir zuerst dafür geschrieben haben, lautete "lass die Quelle sich auf N Inseln ausbreiten". Dieses Ziel erwies sich als ein Versprechen, das niemand halten konnte.

## Die Messung

Das Ziel wurde in sieben Stufen verwendet. In sechs davon haben wir das beste Spiel, das uns einfiel, als Skript abgebildet: die Quelle bei Tick 0 erobern und dann 900 Ticks in Ruhe lassen, jeweils mit vier Seeds. (14-8 lässt sich so nicht skripten, weil der Gegner die Quelle von Anfang an hält.)

| Stufe | Nötige Ausbreitungen | Erzielte Ausbreitungen |
|---|---|---|
| 14-1 | 2 | 0 |
| 14-2 | 2 | 0 |
| 14-3 | 3 | 0 |
| 14-5 | 2 | 0 |
| 14-6 | 2 | 0 |
| 14-7 | 3 | 0 |

Der Gegner nimmt die kleinen Inseln neben der Quelle zwischen Tick 70 und Tick 250. Der erste Puls kommt bei Tick 150 oder später, sodass oft nichts mehr übrig ist, worauf er sich ausbreiten könnte.

## Drei Dinge, die wir versucht haben

1. **Die Inseln verschieben.** Eine Suche über kleine Inseln neben der Quelle fand Anordnungen, die in 14-1 und 14-5 die nötige Zahl erreichen, aber nur, wenn vier oder fünf kleine Inseln neben der Quelle liegen. Das sprengt unsere eigene Obergrenze von drei, und 14-5 verfehlt dann die Untergrenze "der einfachste Bot muss mindestens ein paar Mal gewinnen". Innerhalb der Obergrenze ergab keine Anordnung mehr als eine Ausbreitung.
2. **Den ersten Puls früher kommen lassen.** Mit dem ersten Puls bei 60 Ticks wird 14-1 möglich, und die anderen fünf Stufen bleiben bei 0 oder 1. Außerdem drückte es 14-8 für den einfachsten Bot unter unsere Untergrenze. Wir haben es nicht behalten.
3. **Die Regel ändern.** Das Ziel sollte belohnen, was der Spieler steuert: das Halten der Quelle. Also wurde das Drei-Sterne-Ziel zur **Anzahl der Pulse deiner eigenen Quelle**. Die Zahlen sind auf oder unter dem Wert gewählt, den Bots in gewonnenen Partien tatsächlich erreichten: 14-1: 4, 14-2: 3, 14-3: 2, 14-5: 3, 14-6: 1, 14-7: 3, 14-8: 1. Stufe 14-4 behält ihr eigenes Ziel.

Wir haben uns für die dritte entschieden. Sie betrifft nur Meer 14, daher haben sich die Hashes und Golden-Dateien der Meere 1 bis 13 nicht geändert.

## Ein letzter Durchgang durch das Meer

Nebenbei haben wir die Mitte von 14-1 verbreitert (eine zentrale Insel von 4 auf 12) und 14-6 entschärft, wo ein Bot weit mehr gewann als die anderen. Ein neuer Test besagt nun, dass in 14-8 kein einzelner Bot mehr als die Hälfte der Siege holen darf; heute sind es 8, 17, 12 und 24 Siege für vier Bots und 0 für den fünften.

## Was wir nicht geprüft haben

- In 14-6 und 14-8 hält der Gegner die Quelle, also ist ein Puls das Höchste, womit man rechnen kann. Bots erreichten sie selten, die Zahlen beruhen daher auf dünner Datenlage. **[nicht verifiziert]**
- Niemand hat diese Stufen von Hand gespielt. Ob "lass die Quelle pulsieren" auf der Stufenkarte und im Ergebnisbildschirm verständlich ist, muss auf einem echten Handy geprüft werden. **[nicht verifiziert]**
- Das Spiel ist in Entwicklung und nicht veröffentlicht.
