---
title: Eine Taste, die der Screenreader betätigen kann
description: Das Schließen-Symbol und der Leuchtturm in Inkisle hatten vorgelesene Namen, aber ihre Bedienaktionen fehlten. Wir haben die Beschriftung und die Wirkung beim Auslösen der Taste geprüft.
slug: a-button-the-screen-reader-can-press
lang: de
translation_of: en
category: making-of
keywords: Inkisle, Barrierefreiheit, Screenreader, Oberfläche, Widget-Tests
image_alt: Auf zwei kleinen Karten stehen ein X und ein Leuchtturm. Ein Fokusring umgibt jedes Symbol.
---

Inkisle ist ein Strategiespiel zur Eroberung von Inseln, das noch in Entwicklung ist. Bei einer Prüfung der Barrierefreiheit haben wir untersucht, wie das Spiel seine Bedienelemente an einen Screenreader übermittelt. Zwei fielen auf: das X zum Schließen eines Fensters und der Leuchtturm auf der Karte, über den man ein Ende erneut abspielen kann. Wir entwickeln das Spiel für iOS.

## Vom Namen zur Aktion

Beide Bedienelemente hatten schon einen Namen. Als wir die Standardbeschreibung des Symbols ersetzt hatten, war im Barrierefreiheitsbaum von Flutter am Knoten mit dem Namen auch die Aktion zum Antippen verschwunden. Wir haben die Aktion am selben Knoten wie die Beschriftung hinterlegt. In den Tests schließt die Aktion Schließen das Fenster, und der Leuchtturm öffnet das Ende.

## Einmal hören genügt

Wir haben auch geprüft, was doppelt vorgelesen wurde. Eine Taste für den Anteil der Flotte gab denselben Prozentwert in ihrer Beschriftung und im sichtbaren Text an. Ähnlich war es beim Überspringen des Intros und bei den nummerierten Markierungen der Karte. Jedes Bedienelement hat nun genau eine gesprochene Beschriftung mit den Angaben, die man zum Erkennen braucht.

## Häufige Fragen (FAQ)

### Wurde das mit einem Screenreader auf einem Telefon getestet?

Die Widget-Tests haben die Beschriftungen und Bedienaktionen geprüft. Auf einem Telefon haben wir die Änderungen mit VoiceOver oder TalkBack noch nicht überprüft.

### Wozu dient der Leuchtturm auf der Karte?

Wenn du ihn betätigst, kannst du ein Ende noch einmal ansehen.
