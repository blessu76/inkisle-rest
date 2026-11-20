---
title: Une fin qui ne se joue qu'une fois, et un phare pour la revoir
description: La fin de la saison 1 d'Inkisle se joue d'elle-même exactement une fois, la première fois que la dernière étape de l'acte 30 est réussie. Comment nous avons fixé les règles de relecture, comment sont traités les joueurs qui l'ont déjà terminée et la fin de l'acte 10, et ce que nous n'avons pas vérifié sur les traductions ni sur un appareil réel.
slug: an-ending-that-plays-once
lang: fr
translation_of: en
category: making-of
keywords: Inkisle, saison 1, fin, fin ouverte, phare, game design, jeu mobile
image_alt: Une île solitaire sur une mer calme avec un phare allumé, et la route de la carte marine qui s'arrête devant lui.
---

La fin de la saison 1 d'Inkisle, notre jeu de stratégie de conquête d'îles pour iOS, se joue d'elle-même une fois, la première fois que l'étape 8 de l'acte 30 est réussie. Pour la revoir, le joueur touche le phare en haut de l'acte 30. La fin n'a pas de mot de clôture ; la seule marque est « Inkisle · Season 1 ». Cet article parle moins de ce que montre la fin que du moment où elle se joue et de celui où elle ne se joue pas, et de la façon dont nous avons fixé ces règles. Le jeu est en développement et n'est pas sorti.

## Quatre règles

Voici les règles de relecture que nous avons fixées à l'ajout de la fin.

- **Une fois, à la première réussite.** Elle se joue d'elle-même au moment où l'étape 8 de l'acte 30 est gagnée pour la première fois.
- **Plus jamais d'elle-même.** Regagner la même étape ou redémarrer l'app ne la lance pas automatiquement.
- **Passable à tout moment.** Un toucher mène à l'image finale fixe, et un appareil avec la réduction des animations activée démarre sur l'image fixe.
- **La relecture, c'est le phare.** Un phare se trouve en haut de l'acte 30, et le toucher rejoue la même fin.

Même quand une fin dure moins de 30 secondes, nous avons décidé que « une fois, juste après la victoire » est un cadeau et que « à chaque victoire » est une interruption.

## Où est écrit « déjà vu »

Le fait qu'elle ait été jouée est conservé comme clé d'histoire dans les données de sauvegarde. La clé de la fin de saison est **volontairement distincte** de la clé de la fin de l'acte 10. Si les deux utilisaient une seule clé, un joueur ayant vu la fin de l'acte 10 pourrait voir la fin de saison comptée comme déjà vue. Un test le vérifie : regarder la fin de l'acte 10 laisse la clé de saison intacte.

## Les joueurs qui l'ont déjà terminée

Quelqu'un peut avoir réussi l'étape 8 de l'acte 30 avant que la fin n'existe. Pour cette sauvegarde, le moment de la première réussite est déjà passé : rien ne se joue d'office et seul le phare apparaît. Nous avons choisi de ne pas forcer un moment révolu et de laisser le joueur appuyer quand il le souhaite.

Dans le même changement, le phare de l'acte 10 a été déplacé en haut de l'acte 10, là où il doit être.

## Ce que fixent les tests

La fin a 18 tests. Ceux liés à ces règles :

- Elle se joue exactement une fois à la première victoire de l'étape 8 de l'acte 30, et pas quand le joueur y retourne.
- Rien ne se joue à l'étape 7 de l'acte 30 ni à l'étape 8 de l'acte 29.
- Une sauvegarde qui a déjà réussi l'étape 8 de l'acte 30 n'a pas de lecture automatique, seulement le phare.
- À 375px et 320px, dans les tests de widgets, lecture, saut et sortie en cours de route fonctionnent.
- Le texte des 12 langues tient sans débordement.

## Pas de mot de clôture

La dernière ligne, en coréen, est « L'eau profonde se reflète. » (「깊은 물이 비친다.」). Aucune version linguistique ne porte un mot comme « Fin », et la marque du bas est « Inkisle · Season 1 ». Les règles de relecture viennent de la même idée : l'histoire se ferme, mais pas l'app. Après l'acte 30, les joueurs peuvent encore rejouer des actes, collecter trois étoiles et consulter les tableaux des scores.

## Ce que nous n'avons pas vérifié

- **Le texte de la fin dans les 10 langues autres que le coréen et l'anglais est traduit automatiquement et n'a pas été relu.** Avec seulement quelques lignes à l'écran, la qualité d'une traduction se voit tout de suite.
- Le fondu lent, les lettres dorées et le volume de la cloche n'ont pas été vus sur un appareil réel.
- Les rendus en 375px et 320px n'ont été vérifiés que dans des tests de widgets, dont la police de test est bien plus large que la vraie.
- L'existence d'une saison 2 n'est pas décidée, et aucune date de sortie n'est fixée.

## FAQ

### Combien de fois la fin se joue-t-elle d'elle-même ?

Une fois, la première fois que l'étape 8 de l'acte 30 est réussie. Ensuite, le joueur touche le phare en haut de l'acte 30 pour la revoir.

### Peut-on passer la fin ?

Oui. Un toucher saute à l'image finale fixe, et avec la réduction des animations activée, elle démarre sur l'image fixe.

### Le texte de la fin est-il relu dans toutes les langues ?

Non. Les traductions autres que le coréen et l'anglais sont automatiques et pas encore relues.
