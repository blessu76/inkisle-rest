---
title: Ein Ende, das nur einmal läuft, und ein Leuchtturm, um es wiederzusehen
description: Das Ende von Staffel 1 von Inkisle läuft genau einmal von selbst, wenn die letzte Stufe von Akt 30 zum ersten Mal geschafft wird. Wie wir die Wiedergaberegeln festgelegt haben, wie Spieler behandelt werden, die schon durch sind, und das Ende von Akt 10, und was wir bei Übersetzungen und auf einem echten Gerät noch nicht geprüft haben.
slug: an-ending-that-plays-once
lang: de
translation_of: en
category: making-of
keywords: Inkisle, Staffel 1, Ende, offenes Ende, Leuchtturm, Spieldesign, Mobile Game
image_alt: Eine einsame Insel auf ruhiger See mit einem brennenden Leuchtturm, und die Seekartenroute endet vor ihm.
---

Das Ende von Staffel 1 von Inkisle, unserem Strategiespiel über die Eroberung von Inseln für iOS, läuft einmal von selbst, wenn Stufe 8 von Akt 30 zum ersten Mal geschafft wird. Um es noch einmal zu sehen, tippt der Spieler oben in Akt 30 auf den Leuchtturm. Das Ende hat kein Schlusswort; das einzige Zeichen ist „Inkisle · Season 1“. In diesem Beitrag geht es weniger darum, was das Ende zeigt, sondern wann es läuft und wann nicht, und wie wir diese Regeln festgelegt haben. Das Spiel ist in Entwicklung und nicht veröffentlicht.

## Vier Regeln

Das sind die Wiedergaberegeln, die wir festgelegt haben, als das Ende eingebaut wurde.

- **Einmal, beim ersten Abschluss.** Es läuft von selbst in dem Moment, in dem Stufe 8 von Akt 30 zum ersten Mal gewonnen wird.
- **Nie wieder von selbst.** Dieselbe Stufe erneut zu gewinnen oder die App neu zu starten spielt es nicht automatisch ab.
- **Jederzeit überspringbar.** Ein Tipp führt zum letzten Standbild, und ein Gerät mit eingeschaltetem „Bewegung reduzieren“ beginnt direkt beim Standbild.
- **Wiederholen geht über den Leuchtturm.** Oben in Akt 30 steht ein Leuchtturm, und ein Tipp darauf spielt dasselbe Ende noch einmal ab.

Selbst wenn ein Ende unter 30 Sekunden dauert, haben wir entschieden: „Einmal, direkt nach dem Sieg“ ist ein Geschenk, und „bei jedem Sieg“ ist eine Unterbrechung.

## Wo „schon gesehen“ gespeichert wird

Ob es gelaufen ist, steht als Story-Schlüssel im Spielstand. Der Schlüssel für das Staffelende ist **bewusst getrennt** vom Schlüssel für das Ende von Akt 10. Würden beide einen Schlüssel teilen, könnte bei einem Spieler, der das Ende von Akt 10 gesehen hat, das Staffelende als schon gesehen gelten. Ein Test prüft das: Das Ende von Akt 10 anzusehen lässt den Staffel-Schlüssel unberührt.

## Spieler, die schon durch sind

Jemand kann Stufe 8 von Akt 30 geschafft haben, bevor es das Ende gab. Für diesen Spielstand ist der Moment des ersten Abschlusses schon vorbei, also läuft nichts von selbst und nur der Leuchtturm erscheint. Wir haben uns dagegen entschieden, einen vergangenen Moment zu erzwingen, und lassen den Spieler es drücken, wann er will.

Mit derselben Änderung wurde der Leuchtturm von Akt 10 nach oben in Akt 10 verschoben, wo er hingehört.

## Was die Tests festhalten

Das Ende hat 18 Tests. Die, die an diese Regeln gebunden sind:

- Es läuft genau einmal beim ersten Sieg in Stufe 8 von Akt 30 und nicht, wenn der Spieler erneut hineingeht.
- Bei Stufe 7 von Akt 30 oder Stufe 8 von Akt 29 läuft nichts.
- Ein Spielstand, der Stufe 8 von Akt 30 schon geschafft hat, bekommt keine automatische Wiedergabe, nur den Leuchtturm.
- Bei 375px und 320px funktionieren in Widget-Tests Abspielen, Überspringen und das Verlassen mittendrin.
- Der Text in allen 12 Sprachen passt ohne Überlauf.

## Kein Schlusswort

Die letzte Zeile lautet auf Koreanisch „Die tiefe See spiegelt.“ (「깊은 물이 비친다.」). Keine Sprachversion trägt ein Wort wie „Ende“, und das Zeichen unten ist „Inkisle · Season 1“. Die Wiedergaberegeln folgen demselben Gedanken: Die Geschichte schließt, die App aber nicht. Nach Akt 30 können Spieler weiter Akte wiederholen, drei Sterne sammeln und sich die Bestenlisten ansehen.

## Was wir nicht geprüft haben

- **Der Endtext in den 10 Sprachen außer Koreanisch und Englisch ist maschinell übersetzt und nicht geprüft worden.** Bei nur wenigen Zeilen auf dem Bildschirm fällt die Qualität einer Übersetzung sofort auf.
- Das langsame Ausblenden, die goldene Schrift und die Lautstärke der Glocke wurden nicht auf einem echten Gerät gesehen.
- Die Darstellungen mit 375px und 320px wurden nur in Widget-Tests geprüft, deren Testschrift viel breiter ist als die echte.
- Ob es eine Staffel 2 geben wird, ist offen, und ein Veröffentlichungsdatum steht nicht fest.

## FAQ

### Wie oft läuft das Ende von selbst?

Einmal, wenn Stufe 8 von Akt 30 zum ersten Mal geschafft wird. Danach tippt der Spieler oben in Akt 30 auf den Leuchtturm, um es wiederzusehen.

### Kann man das Ende überspringen?

Ja. Ein Tipp springt zum letzten Standbild, und mit eingeschaltetem „Bewegung reduzieren“ beginnt es beim Standbild.

### Ist der Endtext in jeder Sprache geprüft?

Nein. Übersetzungen außer Koreanisch und Englisch sind maschinell übersetzt und noch nicht geprüft.
