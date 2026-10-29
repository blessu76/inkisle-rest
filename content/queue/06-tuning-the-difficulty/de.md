---
title: Schwierigkeit mit Bots abstimmen: fünf Level, die falsch waren
description: Wir haben jedes Level mit einfachen Bots über je 40 Seeds gespielt und dabei Level gefunden, die unmöglich, zu kurz oder zu schwer waren. Die fünf Änderungen, die Siegquoten davor und danach und warum Bots keine Menschen sind.
slug: tuning-the-difficulty
lang: de
translation_of: en
category: making-of
keywords: Inkisle, Spielbalance, Schwierigkeitsabstimmung, Bot-Simulation, Siegquote, Leveldesign
image_alt: Eine überfüllte Schlacht zwischen mehreren farbigen Seiten im Inkisle-Prototyp.
---
Wir haben noch keine Testspieler, also haben wir eine andere Frage gestellt: Welche Level sind *offensichtlich* falsch? Zwei einfache Bots haben jedes Level je 40 Mal gespielt, mit 40 verschiedenen Seeds, und wir haben die Siegquoten gelesen.

## Die zwei Bots

- **Einfacher Bot:** Alle 10 Ticks greift er die günstigste Insel an, die er besiegen kann. Er steht für einen Gelegenheitsspieler.
- **Geübter Bot:** Alle 5 Ticks sammelt er bis zu drei Inseln und greift gemeinsam an.

Keiner von beiden ist ein Mensch. Sie zeigen uns eine Richtung, nicht die Schwierigkeit, wie ein Mensch sie empfindet.

## Fünf Level, die falsch waren

| Level | Problem | Änderung | Einfacher Bot vorher → nachher |
|---|---|---|---|
| 1-1 | Das Drei-Sterne-Ziel „höchstens 5 verlieren“ war unmöglich: Allein die neutralen Inseln kosteten 13 | Ziel geändert auf „höchstens 14“ | Drei Sterne erreicht 0 % → 100 % |
| 1-5 | In 18 Sekunden vorbei | Gegnerische Basis 20 → 26, eine neutrale Insel an den Gegner gegeben | 100 %, jetzt 30 s |
| 1-8 Boss | Praktisch nicht zu schlagen | Zweite Insel des Gegners verkleinert, Flaggeninsel 24 → 26, eine kleine Insel dem Spieler gegeben | **0 % → 53 %** |
| 2-2 | In 23 Sekunden vorbei | Basis des Spielers 15 → 20, eine Insel an den Gegner gegeben | 100 %, jetzt 38 s |
| 2-8 Boss | Zu schwer | Flaggeninsel 24 → 28, eine gegnerische Festung zu einer neutralen Festung mit 14 gemacht | **10 % → 38 %** |

Die anderen 11 Level haben wir so gelassen. Das Ziel war ein Boss-Level, das ein Gelegenheitsspieler nach etwa einem Neuversuch schafft, also 40 bis 60 % für den einfachen Bot.

## Nebeneffekte, die uns aufgefallen sind

- Über ein Set mit 20 Seeds stieg die Gesamtsiegquote des einfachen Bots von 84 % auf 91 % und die des geübten Bots von 78 % auf 82 %.
- Level 2-2 wurde für den geübten Bot *schwerer*, von 100 % auf 65 %. Wir vermuten, dass der Bot die Angewohnheit hat, Festungen zu leeren, aber das ist **[nicht verifiziert]**.
- Die Level 2-4 und 2-7 zeigen niedrige Siegquoten für den geübten Bot, 40 % und 38 %. In einem dichten Kampf könnte das Sammeln schaden. Ebenfalls **[nicht verifiziert]**.
- Die Zeitlimits für zwei Sterne wirken zu großzügig, da die Bots sie fast immer einhalten. Wir werden sie verschärfen, sobald wir menschliche Zeiten sehen.

![Drei Handy-Bildschirme aus belebten Kämpfen im Prototyp. Der Text in den Screenshots ist Koreanisch.](/assets/posts/img/tuning-boss.jpg)
*Belebte Level im Prototyp: ein Handgemenge mitten im Meer, ein Boss-Level mit umringter Flaggeninsel und ein 320 px breiter Bildschirm.*

## Warum Bots keine Menschen sind

Ein Bot liest nie eine Zahl falsch, langweilt sich nie und zieht nie daneben. Die ersten 30 Minuten eines Menschen sind der wahre Test: wo er es noch einmal versucht, wo er aufgibt, wie lange er bis zu „Weiter“ braucht. Der Plan ist, zuerst ein Spielprotokoll einzubauen und dann fünf bis acht Menschen zu beobachten. Bis dahin sagen diese Zahlen nur, dass kein Level eindeutig kaputt ist, und das ist eine schwächere Aussage als „die Schwierigkeit stimmt“.
