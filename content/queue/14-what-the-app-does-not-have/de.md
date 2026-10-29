---
title: Was die App nicht hat: keine Werbung, keine Konten, kein Tracking
description: Ein Teil des Designs von Inkisle besteht aus dem, was weggelassen wurde. Die App verlangt kein Konto und hat weder Werbung noch Tracking-Werkzeuge, sie läuft auf iOS und Android mit einer gemeinsamen Codebasis, und wir haben für beide ein neues Icon gezeichnet. Was wir entschieden haben und was wir nicht geprüft haben.
slug: what-the-app-does-not-have
lang: de
translation_of: en
category: making-of
keywords: Inkisle, Datenschutz, keine Werbung, kein Konto, App-Icon, iOS, Android, Flutter, Mobile Game
image_alt: Eine korallenfarbene Insel, gezeichnet als einfacher Tintenklecks auf cremefarbenem Hintergrund, das App-Icon von Inkisle.
---
Vieles von dem, was eine App angenehm macht, ist das, was sie **nicht** tut. Für die erste Veröffentlichung von Inkisle haben wir eine kurze Liste von Dingen festgelegt, die wir weglassen.

## Kein Konto, keine Werbung, kein Tracking

- **Kein Konto.** Du öffnest die App und spielst. Es gibt keine Registrierung und keine Anmeldung.
- **Keine Werbung und keine Tracking-Werkzeuge.** Die Liste der externen Pakete der App ist kurz: eines, um kleine Einstellungen auf dem Handy zu speichern, eines zum Abspielen von Sounds und eines zum Öffnen einer Webseite. Es gibt kein Werbepaket, kein Analysepaket und kein Anmeldepaket darin.
- **Der Fortschritt bleibt auf dem Handy.** Die gespeicherten Sterne und die Soundeinstellung werden lokal abgelegt und nirgendwohin gesendet.

Die App hat einen Informationsbildschirm mit einem Link zur Datenschutzerklärung, die dieselbe Seite ist wie auf dieser Website. Das Einzige, was das Netzwerk berührt, ist das Öffnen dieser Seite, und das geschieht nur, wenn der Spieler darauf tippt. Die Erklärung wurde zuerst für diese Website geschrieben, deshalb muss sie noch geprüft und so aktualisiert werden, dass sie die App abdeckt, bevor irgendetwas an einen Store geschickt wird.

## Eine Codebasis, zwei Plattformen

Inkisle ist mit Flutter gebaut, daher werden **iOS und Android gemeinsam entwickelt**, aus demselben Code, und jede Änderung wird für beide getestet. Der Plan ist, **zuerst auf iOS zu veröffentlichen**. Android bauen und testen wir trotzdem die ganze Zeit mit, damit es später nicht zu einem zweiten Projekt wird. Das Spiel ist auf beiden auf Hochformat festgelegt. Die Mindestversionen sind iOS 13 und Android API-Level 24.

## Das Icon

Das Icon ist eine einfache **korallenfarbene Tinteninsel** auf cremefarbenem Hintergrund. Ein einziger Zeichencode erzeugt drei Dateien:

- das normale quadratische Icon für iOS und ältere Android-Versionen,
- den „adaptiven" Vordergrund für Android, gezeichnet innerhalb der 66-%-Sicherheitszone, auf die Android zuschneidet,
- eine einfarbige Silhouette für die Themen-Icons von Android 13.

Wir haben hier einen Fehler ausgeliefert und behoben: Das adaptive Icon wurde doppelt verkleinert (einmal von uns und einmal von den Build-Einstellungen), sodass es auf Android zu klein aussah. Jetzt geschieht die Verkleinerung nur noch an einer Stelle.

## Was wir nicht geprüft haben

- Wir haben die App nicht auf einem **echten iPhone oder Android-Handy** mit einem Store-Build laufen lassen und sie bei keinem der beiden Stores eingereicht. Dinge wie die Store-Prüfung, App-Bildschirme in anderen Sprachen und das Aussehen des Icons in verschiedenen Launchern sind noch offen.
- „Kein Tracking" beschreibt, was in unserem eigenen Code und unserer Paketliste steht. Die Pakete, von denen wir abhängen, haben wir über das Lesen ihrer Beschreibungen hinaus nicht geprüft.
