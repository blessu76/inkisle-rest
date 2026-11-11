---
title: Une courbe de difficulté avec un plancher: aucun niveau que le bot le plus simple ne puisse jamais gagner
description: Avec des centaines de niveaux, quelques niveaux difficiles ne sont pas quelques niveaux difficiles, c'est un mur. Nous avons réglé les 14 mers sur une courbe avec un niveau de repos dans chaque mer, plafonné la force de l'IA ennemie et ajouté un test qui échoue si le bot le plus simple gagne 0 partie sur 40. L'avant et l'après.
slug: a-difficulty-curve-with-a-floor
lang: fr
translation_of: en
category: making-of
keywords: Inkisle, courbe de difficulté, équilibrage du jeu, simulation par bots, conception de niveaux, taux de victoire, niveau d'IA
image_alt: Une rangée sinueuse d'îles qui monte et descend comme une vague, dessinée dans des couleurs vectorielles douces.
published: 2026-11-11T19:00+09:00
---
Un commentaire du propriétaire a changé ce travail : si seulement 40 niveaux sur 800 sont gagnables, le jeu est trop difficile, même si chaque niveau paraît correct isolément. Nous avons donc cessé de régler les niveaux un par un et nous avons écrit une **courbe**.

## La courbe

- Chaque mer compte huit niveaux ayant chacun un **rôle** : ouverture, montée en puissance, niveau de repos, ascension, boss. Le niveau de repos doit être facile : le bot le plus simple doit le gagner au moins 80 % du temps.
- Le taux de victoire visé suit aussi une **vague à travers les volumes** : une mer est un peu plus difficile que la précédente, puis vient de nouveau une mer plus douce.
- Les mers 1 à 3 sont déjà dans les versions TestFlight, nous avons donc laissé leurs valeurs faciles telles quelles.

## Un plafond pour l'ennemi

Certains niveaux étaient difficiles parce que l'IA ennemie était trop maligne, pas parce que la carte était dure. Nous avons ajouté un **plafond d'IA** : le niveau 5 uniquement pour les niveaux comptant plusieurs ennemis, le niveau 4 pour les mers 11 et suivantes, pour les boss et pour le septième niveau à partir de la mer 6, et le niveau 3 partout ailleurs. Toute IA au-dessus de son plafond est abaissée au chargement du niveau. Un exemple : en 10-8, l'amiral est passé du niveau 5 au niveau 3, et la défense du phare neutre de 10 à 5.

## La mesure

Les 14 mers, cinq bots, 40 graines chacun. Le « bot simple » est le plus faible des cinq et tient lieu de joueur humain.

| | Avant | Après |
|---|---|---|
| Niveaux que le bot simple ne gagne jamais | **9** (3-8, 4-3, 4-6, 5-5, 6-8, 7-6, 10-3, 10-8, 14-2) | **0** |
| Niveau le plus faible | 0 victoire sur 40 | 4 victoires sur 40 (8-8), puis 5 sur 40 (10-8) |
| Niveaux de repos, bot simple | non suivi | au moins 80 % |

Quelques exemples de victoires du bot simple sur 40 : 3-8 : 0 → 30. 4-3 : 0 → 18. 6-1 : 2 → 39. 7-6 : 0 → 17.

## Un test qui tient le plancher

`curve_floor_test` échoue si le bot simple gagne 0 partie sur 40 où que ce soit, si un niveau de repos tombe sous 80 %, ou si la moyenne des cinq bots s'écarte trop de la cible de la courbe. Les cibles se trouvent dans un seul fichier : modifier la courbe revient donc à modifier un seul tableau.

## Ce que nous avons volontairement facilité, et le coût

Faciliter les niveaux a donné plus de valeur aux objets d'**Encre**, car un niveau plus facile à gagner profite aussi davantage d'un bonus. Pour conserver les niveaux que nous voulions, nous avons assoupli deux garde-fous de l'Encre : le plafond du taux de victoire d'un boss avec de l'Encre est passé de 55 % à 75 % dans cinq niveaux de boss, et le gain d'une utilisation d'Encre est passé de 25 à 35 points de pourcentage dans quatre niveaux. Ce sont des exceptions que nous avons consignées, et il reste à décider combien l'Encre doit valoir. **[non vérifié en tant que politique]**

## Ce que nous n'avons pas vérifié

- Les taux de victoire viennent de bots. Quelques niveaux (4-6, 5-7, 9-5, 10-2, 10-3, 11-6) s'écartent d'environ dix points de la cible, et 10-8 affiche une moyenne des bots de 62 % pour une cible de 33 %, car l'amiral est très difficile pour le bot le plus simple mais facile pour les autres.
- Personne n'a joué la nouvelle courbe à la main ; le problème « 40 sur 800, c'est trop difficile » n'est donc corrigé que dans les chiffres des bots. **[non vérifié]**
- Le jeu est en développement et n'est pas sorti.
