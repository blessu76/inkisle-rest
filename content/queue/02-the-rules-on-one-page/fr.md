---
title: Les règles sur une page : îles, troupes, conquête
description: Toutes les règles d'Inkisle sur une page : comment les îles produisent des troupes, comment volent les flottes, comment la conquête se calcule et comment une partie se termine. Valeurs de départ, avant les tests.
slug: the-rules-on-one-page
lang: fr
translation_of: en
category: making-of
keywords: Inkisle, règles du jeu, conquête d'îles, moteur déterministe, conception de jeu, règles de conquête
image_alt: Des îles avec des nombres de troupes et des routes en pointillés où voyagent les flottes entre elles.
---
Les bons jeux de stratégie s'expliquent en une minute. Voici notre tentative d'expliquer les règles d'Inkisle sur une page. **Chaque nombre ici est une valeur de départ tirée du document de conception.** Nous comptons en changer certains après les tests, et les articles suivants de cette série montreront lesquels ont déjà changé.

## Les îles produisent des troupes

- Chaque île que vous possédez ajoute **1 troupe par seconde** (un « tick » dure 100 ms, soit une troupe tous les 10 ticks).
- Il y a un **plafond** de 45. Au-delà, l'île cesse de produire, et les troupes en trop issues des renforts retombent vers le plafond à raison de 1 par seconde. Cela vous empêche de tout empiler sur une seule île et d'attendre.
- **Les îles neutres ne produisent pas.** Leur nombre est fixe, il se lit donc comme une étiquette de prix.
- Vous commencez avec une île de départ de 20 troupes. L'ennemi aussi, en général, et sinon la carte du niveau l'indique.

## Envoyer des flottes

Faites glisser votre doigt d'une de vos îles vers une autre île, puis relâchez. Une barre en bas choisit la part : **25, 50, 75 ou 100 %**. Vous envoyez la partie entière des troupes multipliées par la part, au moins 1. À 100 %, vous envoyez « tout moins un », si bien que l'île ne se vide jamais et reste à vous.

Une flotte vole en ligne droite à **2,5 unités de carte par seconde**. Une île voisine à 4 à 8 unités prend environ 1,6 à 3,2 secondes, et traverser toute la carte prend environ 11 secondes. Les flottes ne se battent pas en mer ; elles se croisent. Cela garde l'aperçu d'arrivée honnête, et la tension du genre demeure : un long trajet est un risque, car la cible continue de croître pendant que vous voyagez.

## La conquête, calculée à l'arrivée

- Arriver sur votre propre île ajoute les troupes.
- Arriver sur une île ennemie ou neutre exige de dépasser **la défense multipliée par le coefficient**. Le coefficient vaut 1,0 normalement et **1,5 pour une forteresse**.
- Attaque au-dessus de l'exigence : vous conquérez, et la nouvelle défense est le reste. Égalité : le défenseur tient avec 0 (les égalités reviennent au défenseur). En dessous : le défenseur perd une part.

Deux exemples. Une flotte de 18 arrive sur une forteresse de 10. L'exigence est ceil(10 × 1,5) = 15, vous la conquérez donc avec 3 de reste. Une flotte de 12 arrivant sur la même forteresse la laisse à 2.

Si plusieurs flottes arrivent au même tick, elles sont résolues une par une dans l'ordre de départ.

## Comment une partie se termine

- **Victoire :** l'ennemi n'a plus ni îles ni flottes.
- **Victoire décisive :** si vous avez le triple du total de troupes de l'ennemi et au moins 60 % des îles pendant 5 secondes, l'ennemi abandonne. Cela évite l'ennuyeux nettoyage d'une partie déjà gagnée.
- **Défaite :** vous n'avez plus ni îles ni flottes, ou vous perdez une île que l'on vous avait demandé de protéger.
- **Limite de temps :** à 8 minutes simulées, le joueur qui a le plus d'îles gagne. Cela ne devrait presque jamais se déclencher.

## Un seul moteur pour le temps réel et le tour par tour

L'état du jeu dépend uniquement de la carte de départ, d'une graine et d'une liste de commandes, sans horloge ni hasard dans le moteur. La même entrée donne le même résultat sur chaque appareil. C'est ce qui permet au même moteur de tourner en temps réel aujourd'hui et en tours en réseau plus tard, et de réduire les rediffusions et les rapports de bogues à l'enregistrement d'une liste de commandes.
