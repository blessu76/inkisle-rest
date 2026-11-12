---
title: Une carte marine qui change de route : un style de ligne par mer
description: Avec 14 mers sur une seule carte défilante, la route entre les niveaux paraissait identique partout. Nous avons donné à chaque mer son propre style de ligne, sa couleur et son ondulation, fait en sorte que l'angle se poursuive aux frontières entre mers, et ne dessinons que ce qui est à l'écran. Les valeurs, les tests, et ce que nous n'avons pas encore vu sur un téléphone.
slug: a-chart-that-changes-its-road
lang: fr
translation_of: en
category: making-of
keywords: Inkisle, carte marine, carte des niveaux, style de route, interface mobile, Flutter, performance de rendu
image_alt: Une route pointillée sinueuse entre des îles, qui passe d'une ligne de corde à une ligne d'ondes, dessinée dans des couleurs vectorielles douces.
published: 2026-11-12T19:00+09:00
---
La carte est l'écran où vous passez le temps calme entre les combats : une longue route de niveaux. Avec 14 mers, la route avait le même aspect d'un bout à l'autre. Un long défilement sans changement donne l'impression d'une seule mer répétée. Chaque mer a donc reçu sa propre route.

## Ce qui change selon la mer

| Mer | Ligne | Couleur d'une route terminée |
|---|---|---|
| 1 | pleine (comme avant) | corail |
| 2 | corde | beige voile |
| 3 | longs tirets, pâle | blanc phare |
| 4 | onde | bleu sarcelle |
| 5 | perles | rose corail |
| 6 | longs tirets | or sable |
| 7 | pleine épaisse | bleu marine |
| 8 | pleine fine | cobalt |
| 9 | perles | or lanterne |
| 10 | pleine épaisse | or |
| 11 | pinceau | encre |
| 12 | double ligne | argent |
| 13 | onde | voile blanche |
| 14 | perles | encre profonde |

Chaque mer a aussi son propre balancement (de combien la route oscille sur les côtés, et à quelle fréquence). Sept types de ligne sont partagés entre les 14 mers, et les couleurs sont toutes différentes. La route qui mène à un niveau est dessinée dans le style de la mer à laquelle appartient ce niveau. Après la mer 14, les styles se répètent, à titre provisoire.

## Deux choses qui ne relevaient pas de l'apparence

- **Pas de saut aux frontières entre mers.** Le balancement est une seule fonction continue : l'angle se poursuit donc là où une mer finit et où la suivante commence, et les îles ne sautent pas sur le côté.
- **Ne dessiner que le visible.** La carte aura des centaines de niveaux ; les îles et les routes hors de la zone visible sont donc ignorées. Dans un test de widget, dessiner dix routes visibles a pris moins de 16 ms.

## Les décorations sont venues ensuite

Une deuxième étape a ajouté de petites marques le long de la route pour chaque mer : nœuds, crochets, empreintes de pas, étoiles, gouttes d'encre. Dans les mers 7, 10 et 11, nous les avons ensuite changées en tourbillon, en balise et en étalement, et la goutte de la mer 14 en goutte pointue.

## Tests

Sept tests vérifient que chaque mer a un style, que le balancement reste sous .32, que les 14 couleurs sont toutes différentes, que chaque type de ligne est utilisé, qu'une route terminée a un contraste d'au moins 3:1 avec son bord, que les îles restent entre 18% et 82% de la largeur à 320 px, et que chaque mer dessine des pixels différents. La disposition de la première mer ne bouge pas.

## Ce que nous n'avons pas vérifié

- Tous les rendus jusqu'ici sont des captures de test, où la police est un bloc. Nous ne l'avons pas regardé sur un vrai iPhone ou téléphone Android. **[non vérifié]**
- Nous n'avons pas mesuré le temps de trame avec les 800 niveaux, seulement le contrôle de dix routes. **[non vérifié]**
- Sur les mers nocturnes sombres (11 et 14), la route couleur encre est soutenue par un bord blanc. Savoir si le rendu est bon reste un contrôle de design que nous devons encore faire.
- Le jeu est en développement et n'est pas sorti.
