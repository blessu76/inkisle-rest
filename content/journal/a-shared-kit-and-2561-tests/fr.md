---
title: Ce que nous protégeons en mettant à jour un kit partagé : une barrière de 2 561 tests
description: Chaque fois qu'Inkisle met à jour le kit partagé qu'utilisent nos applications, il doit passer une barrière de format, d'analyse et de tests complets. Pourquoi nous n'avons pas remplacé toute une fonction du kit, comment des tests de temps ont vacillé sous charge, quels fichiers ont changé lors de la dernière mise à jour et ce que nous n'avons pas vérifié.
slug: a-shared-kit-and-2561-tests
lang: fr
translation_of: en
category: making-of
keywords: Inkisle, kit partagé, tests, Game Center, mise à jour, jeu mobile
image_alt: Plusieurs petits blocs de même forme dans un cadre, avec un unique point vert qui passe devant eux.
published: 2026-11-24T12:45+09:00
---

Inkisle, notre jeu de stratégie de conquête d'îles pour iOS, utilise un kit partagé sur lequel s'appuient plusieurs de nos applications. Chaque fois que nous relevons la version du kit, une barrière exécute le format, l'analyse statique et toute la suite de tests avant le commit. Le 19 novembre, nous avons fait passer le kit de 0.15.2 à 0.15.3 : la barrière a validé 2 561 tests (8 ignorés), et seuls deux fichiers ont changé, `pubspec.yaml` et `pubspec.lock`. Cet article raconte comment ce chiffre est tenu et ce qui a vacillé en chemin. Le jeu est en développement et n'est pas sorti.

## La barrière comporte trois étapes

Un script les exécute dans l'ordre avant un commit : le formatage du code ne doit pas changer, l'analyse statique doit signaler 0 problème, et tous les tests doivent passer. Si l'une échoue, nous ne faisons pas de commit. Quand quelqu'un d'autre dit « ça a passé », nous le relançons nous-mêmes avant de faire le commit.

## 14 novembre : nous n'avons pas remplacé toute la fonction du kit

En passant le kit de 0.12.0 à 0.13.0, il pouvait gérer le pseudo et le classement Game Center. La consigne du responsable était que chaque jeu permette au joueur de choisir un pseudo au premier lancement et d'apparaître dans le classement Game Center. Nous n'avons **pas adopté toute la fonction joueur du kit.** Nous avions quatre raisons de juger notre version meilleure :

1. Le pseudo vit dans l'enregistrement des réglages, qui se synchronise entre appareils via iCloud. Le déplacer vers le stockage du kit casserait cette synchronisation.
2. Nous avons déjà une feuille de pseudo en 16 langues et des tests figés sur des combinaisons de langue et de taille d'écran.
3. Les classements sont 24 tableaux dynamiques, dont les valeurs découlent de l'enregistrement de progression synchronisé. Les déplacer laisserait deux endroits qui stockent un meilleur score.
4. Play Games sur Android a toujours besoin de la bibliothèque qu'il utilise.

Seule la connexion Game Center d'iOS est donc passée au kit, et les identifiants de tableau, les pseudos enregistrés et les meilleurs scores ont été conservés tels quels. Le renvoi d'un arriéré après une connexion tardive et le préremplissage du pseudo avec le nom Game Center sont arrivés en même temps. Nous avons ajouté 10 tests, et la barrière a alors validé 1 990 tests (7 ignorés).

## Des tests de temps ont vacillé

À deux reprises dans cette barrière, un test qui mesure le temps a vacillé sous charge. Un test de budget d'images qui dessine 800 routes a échoué une fois quand les tests tournaient en parallèle, et pendant le travail sur iCloud, un test de budget de performance a échoué une fois. Les deux ont passé seuls ou quand la suite complète a été relancée. Nous y voyons de la charge, pas notre changement, mais nous n'avons pas remonté jusqu'à la cause. Nous n'avons pas assoupli les budgets.

## 19 novembre : deux fichiers modifiés

La version 0.15.3 laisse l'API publique telle quelle ; elle fait qu'un recomptage dans la synchronisation iCloud s'arrête après le démontage et ajoute de la documentation. Nous n'avons changé ni code ni tests dans l'application. La limite de taille qu'utilise l'application (512 Ko) est voulue, nous l'avons donc gardée. Les fichiers modifiés étaient `pubspec.yaml` et `pubspec.lock`, et la barrière a passé dès le premier essai, sans vacillement de temps cette fois. Le nombre de tests est passé de 1 990 le 14 novembre à 2 561.

## Ce que nous n'avons pas vérifié

- **La connexion à Game Center, l'envoi des scores, l'écran de classement et un aller-retour iCloud n'ont pas été vérifiés sur un appareil réel.** Nous regarderons dans TestFlight.
- Les rendus en 375 px et 320 px ont été couverts par des tests de widgets à 320×568, et non vus directement.
- Nous n'avons pas trouvé la cause racine des tests qui ont vacillé sous charge.
- Les chiffres ici sont les résultats de la barrière ce jour-là, et le nombre de tests changera plus tard.

## Questions fréquentes

### Qu'est-ce que le kit partagé ?

Un ensemble de code que plusieurs de nos applications utilisent ensemble. Inkisle en utilise les parties pseudo, Game Center et synchronisation iCloud.

### Que vérifiez-vous en mettant à jour le kit ?

Un script vérifie que le formatage ne change pas, que l'analyse statique signale 0 problème et que tous les tests passent. Si l'une échoue, nous ne faisons pas de commit.

### Le jeu est-il sorti ?

Non. Il est encore en développement et n'est pas sorti.
