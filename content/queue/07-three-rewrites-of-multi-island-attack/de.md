---
title: Von mehreren Inseln gleichzeitig senden: drei Neufassungen einer Steuerung
description: Eine Insel von mehreren eigenen aus anzugreifen war die schwierigste Steuerung in Inkisle. Die erste Version per Ziehen, die Korrektur mit Antippen zum Auswählen und die Version mit Wischen zum Auswählen, und was jede uns gelehrt hat.
slug: three-rewrites-of-multi-island-attack
lang: de
translation_of: en
category: making-of
keywords: Inkisle, Touch-Steuerung, Mobile-Game-UX, Mehrfachauswahl, Drag and Drop, Spieldesign, Iteration
image_alt: Eine Schlacht, in der mehrere Inseln Flotten zu einer gegnerischen Insel schicken.
---
Eine Flotte zu schicken ist einfach: von der eigenen Insel zum Ziel ziehen. Das Schwierige an Inkisles Steuerung ist, **von mehreren Inseln gleichzeitig zu senden**, denn späte Level gewinnt man, indem man gemeinsam ankommt. Wir haben diese Steuerung in wenigen Stunden dreimal neu geschrieben, und die Geschichte zeigt, warum.

## v0.1: alles auf einmal

Der erste Prototyp unterstützte mehrere Wege:

- Von einer Insel zu einem Ziel ziehen und **unterwegs über die anderen eigenen Inseln streichen**, um sie als Quellen hinzuzufügen.
- Eine Insel **lange drücken** (0,4 Sekunden), um alle eigenen auszuwählen, und dann für einen Generalangriff ziehen.
- Eine Quelle antippen, dann das Ziel antippen, als Alternative zum Ziehen.

Auf dem Papier deckte das alles ab. In der Praxis verdeckt ein Daumen genau die Insel, über die er gerade streicht, und ein Level, das „beim Ziehen über Inseln streichen“ beibrachte, verlangte eine Geste, die schwer zu sehen und schwer zu treffen ist.

## v0.1.1: erst auswählen, dann losschicken

Die Lösung war, die Geste in zwei Teile zu teilen. **Tippe deine Inseln einzeln an, um sie auszuwählen**, tippe dann das Ziel an, und alle brechen auf. Das Ziehen einer ausgewählten Insel schickt weiterhin die ganze Gruppe. Wir haben hinzugefügt:

- ein kleines Abzeichen über der Auswahl, das zeigt, wie viele Inseln gewählt sind,
- ein Antippen des leeren Meeres, um die Auswahl aufzuheben,
- einen größeren Auswahlbereich beim Hinzufügen während des Ziehens (Inselradius plus 12 px), weil ein Finger größer ist als eine Insel,
- einen Hinweis, der in den ersten Malen angezeigt wird, außerdem beschreiben die Levelkarten, die die Steuerung beibringen, jetzt das Antippen.

Antippen ist präzise und ruhig, aber bei vielen Inseln sind es **viele Taps** vor jedem Angriff. In einem Echtzeitspiel ist das Zeit.

## v0.1.2: Wischen zum Auswählen

Die neueste Version lässt dich **über deine Inseln wischen und sie in einem Strich auswählen**, und dann das Ziel wählen. Vier Inseln auszuwählen ist jetzt eine Bewegung statt vier Taps. Ob die früheren Methoden als Rückfall erhalten bleiben und wie sich das Wischen im Detail anfühlt, ist nicht endgültig **[zum Zeitpunkt des Schreibens nicht verifiziert]**.

## Was wir gelernt haben und was wir nicht wissen

- **Eine Geste, bei der der Finger sich in der Bewegung auf einem kleinen Ziel absetzen muss, ist auf einem Handy fragil.** Die erste Korrektur beseitigte das Zielen, die zweite das Wiederholen.
- Jede Version löste ein Problem und legte das nächste frei, was normal ist, aber auch bedeutet, dass die Steuerung noch nicht feststeht.
- Wir haben **keine Daten von externen Spielern** zu einer der drei Versionen. Das genaue Gefühl von v0.1.2 ist **[nicht verifiziert]**, bis andere es ausprobieren.

Der Test mit fünf bis acht Personen ist der Ort, an dem diese Steuerung wirklich beurteilt wird. Wenn sie vor einem Angriff immer noch zögern, ändern wir sie ein viertes Mal.
