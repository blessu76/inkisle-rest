---
title: La source d'encre de la mer blanche : quand une règle à trois étoiles est impossible à gagner
description: La mer 14 possède une source qui répand de l'encre sur les îles voisines. Les bots n'ont pas réussi l'objectif trois étoiles « faire répandre la source sur N îles » ; nous avons donc mesuré, essayé de déplacer des îles, puis remplacé la règle par un décompte des pulsations de la source. Ce que nous avons essayé et ce qui reste à vérifier.
slug: the-white-sea-ink-spring
lang: fr
translation_of: en
category: making-of
keywords: Inkisle, level design, règle trois étoiles, source d'encre, simulation de bots, équilibrage du jeu, mer 14
image_alt: Une mer pâle avec une petite île-source au centre et quelques îles autour, dessinée dans des couleurs vectorielles douces.
published: 2026-11-10T19:00+09:00
---
La mer 14, la mer blanche, ajoute une règle : une **source d'encre**. Tenez l'île de la source et, tous les 150 ticks, elle pulse et répand de l'encre sur une île voisine. La première pulsation arrive 150 ticks après sa capture. L'objectif trois étoiles que nous avions d'abord écrit pour elle était « faire répandre la source sur N îles ». Cet objectif s'est révélé être une promesse que personne ne pouvait tenir.

## La mesure

L'objectif servait dans sept niveaux. Dans six d'entre eux, nous avons scripté le meilleur jeu auquel nous pouvions penser : capturer la source au tick 0, puis la laisser tranquille pendant 900 ticks, avec quatre graines chacun. (14-8 ne peut pas être scripté ainsi, car l'ennemi tient la source dès le départ.)

| Niveau | Diffusions requises | Diffusions obtenues |
|---|---|---|
| 14-1 | 2 | 0 |
| 14-2 | 2 | 0 |
| 14-3 | 3 | 0 |
| 14-5 | 2 | 0 |
| 14-6 | 2 | 0 |
| 14-7 | 3 | 0 |

L'ennemi prend les petites îles à côté de la source entre le tick 70 et le tick 250. La première pulsation arrive au tick 150 ou plus tard, il ne reste donc souvent plus rien où répandre l'encre.

## Trois choses que nous avons essayées

1. **Déplacer les îles.** Une recherche sur les petites îles à côté de la source a trouvé des agencements qui atteignent le nombre requis dans 14-1 et 14-5, mais seulement en plaçant quatre ou cinq petites îles à côté de la source. Cela dépasse notre propre plafond de trois, et 14-5 ne respecte alors plus le plancher « le bot le plus simple doit gagner au moins quelques fois ». Dans le plafond, aucun agencement n'a donné plus d'une diffusion.
2. **Avancer la première pulsation.** Avec la première pulsation à 60 ticks, 14-1 devient possible et les cinq autres niveaux restent à 0 ou 1. Cela a aussi fait passer 14-8 sous notre plancher pour le bot le plus simple. Nous ne l'avons pas gardé.
3. **Changer la règle.** L'objectif devrait récompenser ce que le joueur contrôle : tenir la source. L'objectif trois étoiles est donc devenu le **nombre de pulsations de votre propre source**. Les valeurs, choisies au niveau ou en dessous de ce que les bots ont réellement atteint dans les parties gagnées : 14-1 : 4, 14-2 : 3, 14-3 : 2, 14-5 : 3, 14-6 : 1, 14-7 : 3, 14-8 : 1. Le niveau 14-4 garde son objectif distinct.

Nous avons choisi la troisième. Elle ne touche que la mer 14, donc les hashes et les fichiers golden des mers 1 à 13 n'ont pas changé.

## Une dernière passe sur la mer

En parallèle, nous avons élargi le milieu de 14-1 (une île centrale passe de 4 à 12) et adouci 14-6, où un bot gagnait bien plus que les autres. Un nouveau test affirme désormais qu'aucun bot ne peut prendre plus de la moitié des victoires dans 14-8 ; aujourd'hui, c'est 8, 17, 12 et 24 victoires pour quatre bots et 0 pour le cinquième.

## Ce que nous n'avons pas vérifié

- Dans 14-6 et 14-8, l'ennemi tient la source, une pulsation est donc le maximum sur lequel on peut compter. Les bots l'ont rarement atteinte, les chiffres reposent donc sur peu de données. **[non vérifié]**
- Personne n'a joué ces niveaux à la main. Savoir si « faire pulser la source » est clair sur la carte du niveau et sur l'écran de résultat demande un vrai téléphone. **[non vérifié]**
- Le jeu est en développement et n'est pas sorti.
