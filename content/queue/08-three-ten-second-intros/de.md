---
title: Ein Zehn-Sekunden-Intro in drei Versionen: Himmel, Meer und Land
description: Inkisle beginnt mit einem Intro von zehn Sekunden, das in drei Versionen existiert. Wie die drei ein gemeinsames Ende teilen, warum ein gemischter Beutel entscheidet, welche du siehst, wann es auf drei Sekunden schrumpft und was bei eingeschalteter Bewegungsreduzierung passiert.
slug: three-ten-second-intros
lang: de
translation_of: en
category: making-of
keywords: Inkisle, Spiel-Intro, App-Start, Überspringen-Button, Bewegung reduzieren, Barrierefreiheit, Mobile Game
image_alt: Inseln in einem mintgrünen Meer, über eine davon breitet sich korallenfarbene Tinte aus, das Eröffnungsbild des Inkisle-Intros.
---
Das Erste, was du beim Öffnen von Inkisle siehst, ist ein Intro. Wir wollten, dass es sich in den ersten Malen wie ein kleines Ereignis anfühlt und danach **nicht im Weg steht**. Dieser Beitrag beschreibt, wie das Intro aufgebaut ist und welche Regeln bestimmen, was du siehst.

## Ein Ende, drei Anfänge

Das vollständige Intro dauert **10 Sekunden**. Die ersten 7 Sekunden gibt es in drei Versionen: **Himmel**, **Meer** und **Land**. Die letzten 3 Sekunden sind in allen gleich: das Ende, das ins Menü führt. Ein gemeinsames Ende heißt, dass wir es nur einmal zeichnen und jede Version am selben Ort ankommt.

## Welche bekommst du?

Zufälliges Auswählen kann dasselbe Intro dreimal hintereinander zeigen, was sich wie ein Fehler anfühlt. Deshalb verwendet die App einen **gemischten Beutel**: Sie legt alle drei Versionen in zufälliger Reihenfolge in einen Beutel und nimmt bei jedem Start eine heraus. Ist der Beutel leer, wird er neu gefüllt. Zwei Folgen:

- Innerhalb einer Runde zeigen **drei Starts hintereinander alle drei Versionen**.
- Die erste Version einer neuen Runde ist nie dieselbe wie die zuletzt gesehene.

Der Beutel wird auf dem Telefon gespeichert und funktioniert deshalb über mehrere Starts hinweg.

## Erst lang, später kurz

Bei den **ersten drei Starts** bekommst du die vollen 10 Sekunden. Ab dem vierten Start spielt die App nur das gemeinsame Ende ab, **3 Sekunden**. Ein Überspringen-Button erscheint **0,6 Sekunden** nach Beginn des Intros, damit niemand beim ersten Mal zum Überspringen aufgefordert wird, bevor er etwas gesehen hat. Überspringen ruft denselben „Fertig"-Schritt auf wie das reguläre Ende des Intros, und ein Test prüft, dass er nur einmal ausgeführt wird.

## Bewegung reduzieren

Ist die Einstellung zur Bewegungsreduzierung des Telefons eingeschaltet (iOS „Bewegung reduzieren" oder ausgeschaltete Animationen unter Android), **bewegt sich das Intro nicht**. Es zeigt das fertige Endbild für **1,2 Sekunden** und wechselt dann ins Menü. Der Überspringen-Button ist von Anfang an da.

## Wenn der gespeicherte Beutel kaputt ist

Unser Code-Review hat ergeben, dass ein beschädigter gespeicherter Beutel nie repariert wurde: Die App konnte ihn nicht lesen, begann bei jedem Start von vorn und zeigte weiterhin die volle 10-Sekunden-Version. Die Lösung: Unlesbare Daten gelten als „keine Daten", und sofort wird ein neuer Beutel geschrieben. Ist der Speicher gar nicht verfügbar, wählt die App eine zufällige Version und spielt das volle Intro, ohne je den Spielstart zu blockieren. Für diese Fälle gibt es Tests.

## Was wir nicht geprüft haben

- Wir haben nicht gemessen, wie das Intro auf einem **echten Telefon** läuft. Die Tests decken die oben genannten Regeln ab, nicht die Flüssigkeit der Animation.
- Ob zehn Sekunden die richtige Länge für den ersten Start sind, bleibt eine Vermutung, bis andere Leute es gesehen haben.
