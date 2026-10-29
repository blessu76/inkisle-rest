---
title: L'encre qui se répand : les petits effets qui disent ce qui vient de se passer
description: Dans Inkisle, une île capturée laisse une tache d'encre, une remontée affiche une bannière et la dernière île ennemie s'illumine. À quoi sert chaque effet, combien de temps il dure, et comment fonctionne l'indice du doigt lors de la première partie.
slug: ink-that-spreads
lang: fr
translation_of: en
category: making-of
keywords: Inkisle, sensation de jeu, retour visuel, jeu mobile, indice d'initiation, animation
image_alt: Une tache d'encre couleur corail qui s'étale sur une île capturée pendant que des flottes se déplacent entre d'autres îles.
---
Dans un jeu où il s'agit de teindre la carte à votre couleur, le moment qui compte le plus est celui où **une île change de mains**. S'il ne s'agit que d'un changement de couleur, il est facile de le manquer sur un petit écran. Nous avons donc ajouté quelques petits effets dont le rôle est de dire « cela vient de se produire ».

## La tache de capture

Quand une île change de propriétaire, une **tache d'encre** s'en échappe dans la couleur du nouveau propriétaire, puis s'estompe. Elle dure environ **0,75 seconde**. La forme est une tache irrégulière dessinée de la même façon que les taches de l'intro, ce qui rapproche visuellement le jeu et son ouverture. Un test vérifie qu'une capture laisse une tache et qu'elle disparaît ensuite.

## Trois moments qui reçoivent un message

- **Une remontée.** Quand vous étiez derrière et prenez la tête, une bannière apparaît **une seule fois**. Elle s'affiche environ 1,6 seconde. « Une seule fois » compte : une bannière qui se déclenche à chaque fois que la tête change de camp devient du bruit.
- **La dernière île.** Quand l'ennemi n'a plus que **sa dernière île**, celle-ci est mise en évidence pour que vous sachiez où viser.
- **Terminer une mer.** Terminer toute une mer a son propre court moment, distinct de l'écran de résultat d'un niveau isolé.

## L'indice du doigt de la première partie

Un nouveau joueur ne sait pas qu'on fait glisser le doigt d'une île à une autre. La première fois dans un niveau, un petit **doigt glisse de votre île vers l'île la plus proche**. Il disparaît dès que vous envoyez quoi que ce soit, et un test le vérifie. Nous l'avons gardé petit et bref pour ne pas ralentir un joueur qui connaît déjà la commande.

## Ce que nous n'avons pas vérifié

- Tout cela est couvert par des tests sur **le moment** où un effet apparaît, pas sur **la sensation** qu'il procure. Le rythme, la taille et la couleur sont de premières suppositions, et personne en dehors de l'équipe ne les a essayés sur un vrai téléphone.
- Nous ne savons pas encore si la bannière de remontée encourage ou ne fait que distraire.
