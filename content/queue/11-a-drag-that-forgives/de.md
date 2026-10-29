---
title: Ein verzeihendes Ziehen: die kleinen Regeln hinter einer Geste
description: Eine Flotte zu schicken ist in Inkisle ein einziges Ziehen. Die kleinen Regeln, die es mit einem echten Finger funktionieren lassen: ein größerer Auswahlbereich, ein Ziehen, das den ganzen Weg abtastet, immer nur ein Finger und klare Meldungen, wenn ein Senden nicht möglich ist.
slug: a-drag-that-forgives
lang: de
translation_of: en
category: making-of
keywords: Inkisle, Touch-Steuerung, Mobile-Game-UX, Drag and Drop, Multitouch, Spieldesign
image_alt: Ein Daumen zieht von einer korallenroten Insel über das Meer zu einer Nachbarinsel, dahinter eine gepunktete Linie.
---
Das erste Level lehrt die ganze Steuerung in einer Zeile: **Ziehe eine Insel auf eine andere Insel, und ein Schiff legt ab**. In diesem Satz stecken viele kleine Entscheidungen, denn ein Daumen ist viel ungenauer als eine Maus. Dieser Beitrag sammelt die, bei denen wir uns am sichersten sind.

## Der Finger ist größer als die Insel

Eine Insel auf dem Bildschirm kann kleiner sein als eine Fingerspitze, und der Finger verdeckt sie beim Zielen. Wenn du beim Ziehen über Inseln fährst, gilt deshalb als „auf dieser Insel“ der Bereich **Radius der Insel plus 12 Pixel**. Ohne diesen zusätzlichen Rand verfehlte ein Ziehen, das sichtbar auf einer Insel endete, sie oft.

## Ein schnelles Wischen überspringt keine Insel

Wenn du über mehrere Inseln wischst, um sie auszuwählen, meldet der Bildschirm deinen Finger nur in Abständen. Ein schnelles Wischen konnte von einer Seite einer Insel zur anderen springen, ohne je innerhalb gemeldet zu werden. Das Spiel **tastet deshalb entlang der Linie** zwischen zwei Meldungen ab, sodass jede Insel gezählt wird, die der Finger überquert hat.

## Immer nur ein Finger

Unser erstes Code-Review fand einen Fall, an den wir nicht gedacht hatten: Berührt mitten im Ziehen ein **zweiter Finger** den Bildschirm, ersetzte die zweite Berührung die erste, und die Bewegungen beider Finger vermischten sich. Das konnte die Auswahl in einen seltsamen Zustand bringen oder eine Flotte losschicken, die niemand schicken wollte. Die Lösung ist einfach: Das Spiel folgt **nur dem ersten Finger** und ignoriert die anderen, bis er losgelassen wird. Ein Test deckt ab, dass der zweite Finger ignoriert wird.

## Sagen, warum nichts passiert ist

Wenn du von einer Insel mit zu wenigen Truppen senden willst, findet das Senden nicht statt. Stille fühlt sich wie ein Fehler an, deshalb zeigt das Spiel eine kurze Meldung: Eine Insel braucht **mindestens 2 Truppen**, um zu senden. Hältst du eine Insel **0,4 Sekunden** gedrückt, werden alle deine Inseln ausgewählt, und eine Meldung sagt dir, dass du ein Ziel antippen oder ziehen sollst, um einen Großangriff zu starten.

## Die Menge, die gesendet wird

Wie viel eine Insel verlässt, legt eine Anteilsleiste fest. Standard sind **50 %**. Level 1-2 lehrt die Wahl des Anteils, und sein Drei-Sterne-Ziel ist, **ohne je 100 % zu senden** zu gewinnen, was dich anregt, die anderen Einstellungen auszuprobieren.

## Was wir nicht überprüft haben

- Alles hier wurde mit simulierten Berührungen in Tests geprüft. Wir haben **keine echten Menschen** auf echten Handys dabei beobachtet, und Gesten, die im Test gut aussehen, können sich trotzdem falsch anfühlen.
- Die Größen (12 px, 0,4 s) sind erste Schätzungen. Sie ändern sich, wenn Spielerinnen und Spieler Inseln verfehlen oder aus Versehen alles auswählen.
