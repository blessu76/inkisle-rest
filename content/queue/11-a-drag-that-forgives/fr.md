---
title: Un glissement qui pardonne : les petites règles derrière un geste
description: Envoyer une flotte dans Inkisle se fait d'un seul glissement. Les petites règles qui le font fonctionner avec un vrai doigt : une zone de sélection plus large, un glissement qui échantillonne tout le trajet, un seul doigt à la fois et des messages clairs quand un envoi est impossible.
slug: a-drag-that-forgives
lang: fr
translation_of: en
category: making-of
keywords: Inkisle, commandes tactiles, UX de jeu mobile, glisser-déposer, multitouch, game design
image_alt: Un pouce qui glisse depuis une île corail à travers la mer jusqu'à une île voisine, avec une ligne pointillée derrière lui.
---
Le premier niveau enseigne toute la commande en une ligne : **glissez une île sur une autre île et un navire part**. Cette phrase cache beaucoup de petites décisions, car un pouce est bien plus imprécis qu'une souris. Cet article rassemble celles dont nous sommes les plus sûrs.

## Le doigt est plus grand que l'île

Une île à l'écran peut être plus petite qu'un bout de doigt, et le doigt la recouvre pendant que vous visez. Donc, lorsque vous passez au-dessus d'îles pendant un glissement, la zone qui compte comme « sur cette île » est **le rayon de l'île plus 12 pixels**. Sans cette marge, un glissement qui finissait visiblement sur une île la ratait souvent.

## Un balayage rapide ne peut pas sauter une île

Quand vous balayez plusieurs îles pour les choisir, l'écran ne signale la position de votre doigt qu'à intervalles. Un balayage rapide pouvait sauter d'un côté d'une île à l'autre sans jamais être signalé à l'intérieur. Le jeu **échantillonne donc le long de la ligne** entre deux signalements, de sorte que chaque île traversée par le doigt est comptée.

## Un seul doigt à la fois

Notre première revue de code a trouvé un cas auquel nous n'avions pas pensé : si un **deuxième doigt** touche l'écran au milieu d'un glissement, le deuxième toucher remplaçait le premier, et les mouvements des deux doigts se mélangeaient. La sélection pouvait se retrouver dans un état étrange, ou une flotte que personne ne voulait envoyer partait. La correction est simple : le jeu ne suit que **le premier doigt** et ignore les autres jusqu'à ce qu'il se lève. Un test vérifie que le deuxième doigt est ignoré.

## Dire pourquoi rien ne s'est passé

Si vous essayez d'envoyer depuis une île qui a trop peu de troupes, l'envoi n'a pas lieu. Le silence ressemble à un bug, alors le jeu affiche un court message : une île a besoin d'**au moins 2 troupes** pour envoyer. Un appui long de **0,4 seconde** sur une île sélectionne toutes vos îles, et un message vous invite à toucher ou glisser vers une cible pour une attaque générale.

## La quantité à envoyer

La quantité qui quitte une île est réglée par une barre de proportion. Par défaut, c'est **50 %**. Le niveau 1-2 apprend à choisir la proportion, et son objectif trois étoiles est de gagner **sans jamais envoyer 100 %**, ce qui vous pousse à essayer les autres réglages.

## Ce que nous n'avons pas vérifié

- Tout ce qui est décrit ici est vérifié avec des touchers simulés dans des tests. Nous **n'avons pas observé de vraies personnes** l'utiliser sur de vrais téléphones, et des gestes qui semblent corrects dans un test peuvent quand même être désagréables.
- Les tailles (12 px, 0,4 s) sont de premières estimations. Elles changeront si les joueurs ratent des îles ou sélectionnent tout par accident.
