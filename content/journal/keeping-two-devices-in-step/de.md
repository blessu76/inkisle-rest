---
title: Zwei Geräte im Gleichschritt halten: iCloud-Sync in ein gemeinsames App-Kit verlegt
description: Fortschritt, Tinte und Einstellungen von Inkisle wurden bereits über iCloud zwischen Geräten abgeglichen. Am 16. November haben wir diese Brücke in ein gemeinsames App-Kit verlegt. Wie wir gespeicherte Daten heil gehalten haben, welche Zusammenführungsregeln nie schrumpfen, wie die Kaufmarkierung behandelt wird und was wir auf echten Geräten noch nicht geprüft haben.
slug: keeping-two-devices-in-step
lang: de
translation_of: en
category: making-of
keywords: Inkisle, iCloud, geräteübergreifende Synchronisierung, Spielstand, Zusammenführen, Mobile Game
image_alt: Zwei Bildschirme unterschiedlicher Größe, durch einen dünnen Faden verbunden, mit gleich gefärbten Inseln auf beiden Karten.
published: 2026-11-23T13:45+09:00
---

In Inkisle, unserem Strategiespiel über die Eroberung von Inseln für iOS, werden Fortschritt, Tinte und wichtige Einstellungen (Sprache und Spitzname) über den eigenen iCloud-Schlüssel-Wert-Speicher des Spielers zwischen Geräten mit derselben Apple-ID abgeglichen. Diese Synchronisierung gab es schon. Am 16. November haben wir sie nicht gebaut, sondern eine selbst geschriebene Brücke in ein gemeinsames App-Kit verlegt, und die größte Sorge war, keinen einzigen gespeicherten Wert zu verlieren. Einen Round Trip zwischen einem echten iPhone und iPad haben wir noch nicht geprüft. Das Spiel ist in Entwicklung und nicht veröffentlicht.

## Was wir verlegt haben

Die Anweisung des Verantwortlichen an diesem Tag lautete, dass das Synchronisieren von Spieldaten zwischen Apple-Geräten verpflichtend sein und in das gemeinsame App-Kit gehören soll. Wir fanden die iCloud-Schlüssel-Wert-Berechtigung bereits eingeschaltet und eine eigene Swift-Brücke samt Speicher-Wrapper in der App. Also:

| Teil | Was sich geändert hat |
|---|---|
| Brücke | Unsere eigene Swift-Brücke und den Wrapper gelöscht und auf den Plattformspeicher des Kits umgestellt: iCloud unter iOS, sonst nur lokal |
| Schlüssel und Kodierung | Speicherschlüssel, Zeichenkettenkodierung und Speicherkennung unverändert gelassen |
| Vor dem Lesen | Unter iOS die Synchronisierung direkt vor einem Lesevorgang einmal anstoßen (die Synchronisierung läuft weiter, auch wenn das fehlschlägt) |
| Projekteinstellungen | Die iCloud-Fähigkeit auch in die Projektdatei eingetragen |

## Keine Daten verlieren

Weil Schlüssel und Formate gleich blieben, liest der neue Build, was der alte geschrieben hat, und der alte Build liest, was der neue schreibt. Beide Richtungen haben wir mit Tests festgenagelt: einen Block im alten Format mit dem neuen Code lesen, einen neuen Block mit dem alten Code lesen und einen alten Einstellungsblock lesen. Es wurde nur Code gelöscht; gespeicherte Werte wurden nicht angetastet.

## Zusammenführen schrumpft nie

Wenn zwei Geräte unterschiedlichen Fortschritt haben, haben wir die eigene Zusammenführung der App beibehalten. Das Kit hat auch einen Merger, den wir aber nicht benutzt haben. Die Zusammenführung der App wächst bereits nur, und mit denselben Schlüsseln und demselben Format war es sicherer, sie unangetastet zu lassen.

- Sterne und Bestwerte pro Stufe nehmen den größeren Wert.
- Beim Fortschritt zählt das Gerät, das weiter ist; Tinte und Einstellungen werden nur vereint, nie verkleinert.
- Weicht der Wert in der Cloud von dem ab, den wir zuletzt hochgeladen haben, laden wir erneut hoch, um uns von einem alten Build zu erholen, der denselben Schlüssel überschrieben hat.

## Was mit der Kaufmarkierung geschah

Ein früherer Beitrag sagte, dass die Freischaltung nicht auf ein anderes Gerät übergeht. Diese Arbeit hat das geändert. Der Sync-Block trägt jetzt eine Markierung, dass Alle Meere freischalten gekauft wurde, und ein anderes Gerät, das sie liest, öffnet ebenfalls. Die Markierung **wächst nur.** Ein Block ohne sie nimmt sie nicht weg; wir laden sie erneut hoch.

Das ist eine Designänderung nach der Anweisung des Verantwortlichen zur „verpflichtenden Synchronisierung“, und sie hat eine Grenze: Ist die Markierung einmal synchronisiert, nimmt eine Erstattung sie auf anderen Geräten nicht zurück. Wie wir mit Erstattungen umgehen, bleibt eine Entscheidung der Richtlinie. Auch der Kaufablauf selbst wurde noch nicht auf einem echten Gerät durchgespielt.

## Größe und Tests

Der iCloud-Schlüssel-Wert-Speicher hat ein Gesamtlimit (1 MB). Der Sync-Block für einen Spielstand mit allen 240 abgeschlossenen Stufen ist etwa 6,3 KB groß, und ein Test hält ihn unter 16 KB. Die 14 neuen Tests decken unveränderte Schlüssel und Kodierung ab, das Zusammenführen zweier Geräte, die Ausbreitung der Kaufmarkierung ohne Rücknahme, das Lokalbleiben offline oder ohne Anmeldung und das Zusammenführen nach der Rückkehr online. Über die vier Cloud-Testdateien hinweg bestanden 77 Tests.

## Was wir nicht geprüft haben

- **Eine echte Synchronisierung zwischen iPhone und iPad wurde nicht geprüft.** Sie lässt sich nur auf echten Geräten oder über TestFlight sehen.
- Löschungen wandern nicht auf andere Geräte, weil diese Synchronisierung nur zusammenführt.
- Android ist nicht betroffen. Die Daten bleiben auf dem Gerät.
- Überschreibt ein alter Build auf einem anderen Gerät denselben Schlüssel, kann die Kaufmarkierung kurz verschwinden, und der neue Build lädt sie erneut hoch.
- Die Datenschutzerklärung beschreibt diese Synchronisierung jetzt: Spieldaten liegen in der eigenen iCloud des Spielers, nicht auf unseren Servern, und lassen sich in den Geräteeinstellungen abschalten.

## FAQ

### Wird der Inkisle-Fortschritt auf einem Server gespeichert?

Nein. Er wird über den eigenen iCloud-Schlüssel-Wert-Speicher des Spielers zwischen Geräten mit derselben Apple-ID abgeglichen und nicht an unsere Server gesendet.

### Lässt sich die Synchronisierung abschalten?

Ja. Wer iCloud für diese App in den iOS-Einstellungen ausschaltet, stoppt die Synchronisierung, und die Daten bleiben nur auf dem Gerät.

### Wird auf Android synchronisiert?

Nein. Unter Android bleiben die Daten auf dem Gerät.
