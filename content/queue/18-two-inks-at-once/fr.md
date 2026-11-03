---
title: Deux objets d'encre à la fois : emplacements, délais et ce que les bots nous ont appris
description: Dans les premières mers, on ne pouvait utiliser qu'un objet d'encre à la fois. À partir de la mer 5, on peut en utiliser deux, puis trois, avec un délai entre les départs. Le tableau des règles, la façon dont le bouton l'affiche, et une simulation qui a trouvé un effet bien plus faible que prévu.
slug: two-inks-at-once
lang: fr
translation_of: en
category: making-of
keywords: Inkisle, objets d'encre, conception de jeu, équilibrage, simulation par bots, interface mobile, accessibilité
image_alt: Deux petites gouttes d'encre côte à côte au-dessus d'une rangée d'îles, dessinées dans des couleurs vectorielles douces.
---
Les objets d'encre (afflux, ancre, brume, lanterne, inversion de marée) fonctionnaient un par un. C'est facile à comprendre, mais cela veut aussi dire qu'un niveau avancé ne donne jamais l'impression d'avoir plus d'outils. Nous avons donc donné des **emplacements** au bouton d'encre.

## La règle

| Mer | Emplacements simultanés | Délai entre les départs |
|---|---|---|
| 1 à 4 | 1 | aucun (comme avant) |
| 5 à 10 | 2 | 10 secondes |
| Volume 2, mers 11 à 20 | 2 | 5 secondes |
| Volume 3, à partir de la mer 21 | 3 | 5 secondes |

Ce qui ne change pas : un boss ajoute 5 secondes au délai ; la limite d'utilisations par niveau (5 ou 6) est partagée par tous les emplacements ; on ne peut pas lancer deux objets du même type ; l'emplacement d'une ancre ou d'une brume est libéré quand son île est capturée ; et les 20 premières secondes d'un niveau verrouillent toujours toute l'encre.

## Comment le bouton l'affiche

Le bouton d'encre a un point par emplacement, rempli tant que l'emplacement est utilisé. Un fin anneau à l'intérieur du bouton compte le délai avant de pouvoir lancer le suivant. Dans la fiche du port, une carte bloquée indique « prochaine encre dans N secondes » pendant le délai, ou « en cours de diffusion » quand les emplacements sont pleins. L'étiquette d'accessibilité se lit par exemple « 1 emplacement sur 2 ». Tout cela existe en 12 langues.

## Pourquoi le moteur n'a pas eu besoin d'un nouveau hash

L'état du jeu contient déjà une liste des heures de fin de l'encre en cours et le nombre d'utilisations, si bien que les mers 1 à 4 se comportent et produisent leur hash exactement comme avant. Les tests couvrent chaque ligne du tableau, le comportement de la première mer, le refus d'un même type, les emplacements pleins, trois emplacements, la limite partagée et la libération à la capture, ainsi que le bouton à 320 et 375 px.

## Ce que les bots ont dit

Nous avons simulé 80 niveaux, de la mer 5 à la mer 14, avec cinq bots et 24 graines chacun, pour quatre plans de deux ou trois objets commençant à 20 secondes, et comparé le meilleur plan sous l'ancienne règle (un emplacement, sans délai) à la nouvelle règle.

- Le gain moyen est de **+1,1 point de pourcentage** (+0,9 dans les mers 5 à 10, +1,5 dans les mers 11 à 14). Nous en attendions 3 à 8.
- Contre les boss, il est de +0,9. Le meilleur taux de victoire avec encre par rapport à sans encre est de +36 points, dans notre limite de 40.
- Niveau par niveau, le changement a varié entre −7 et +10, soit à peu près le bruit de 24 graines.

Les bots utilisent rarement bien le deuxième emplacement, donc ce petit chiffre en dit peut-être plus sur les bots que sur la règle. **[non vérifié]** Une personne pourrait gagner davantage.

## Ce que nous n'avons pas vérifié

- Si une personne trouve les deux emplacements et le délai clairs, ou si cela ressemble à un verrou. Nous ne l'avons pas testé sur un vrai téléphone. **[non vérifié]**
- Un message d'une ligne la première fois qu'un joueur atteint une mer à deux emplacements (5-1) n'est pas encore réalisé.
- Le jeu est en développement et n'est pas publié.
