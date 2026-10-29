---
title: Un prototype jouable en une journée
description: Seize niveaux, deux mers et un seul fichier HTML d'environ 95 Ko sans requête externe. Comment le prototype est construit, ce que nous avons testé dans un navigateur sans interface et ce que nous n'avons pas pu tester.
slug: a-playable-prototype-in-a-day
lang: fr
translation_of: en
category: making-of
keywords: Inkisle, prototype, prototype web, moteur de jeu déterministe, jeu HTML, jeu mobile, canvas
image_alt: De nombreuses petites îles portant des nombres de troupes et une flotte traversant la mer dans le prototype d'Inkisle.
---
Avant de construire une application, nous voulions quelque chose de jouable sur un téléphone. Le 2026-10-29, nous avons construit un prototype web en une seule journée. Cet article décrit ce qu'il contient, comment il est assemblé et, tout aussi important, ce que nous n'avons pas pu vérifier.

![Trois écrans de téléphone du prototype : la carte marine avec une fiche de niveau, une bataille avec un glissement en cours et un résultat de victoire avec trois étoiles. Le texte dans les captures d'écran est en coréen.](/assets/posts/img/proto-shots.jpg)
*La carte marine avec une fiche de niveau, une bataille avec un glissement en cours et l'écran de résultat.*

## Ce qu'il contient

- **Seize niveaux :** la mer 1, « Baie calme » (Calm Bay), en compte huit, et la mer 2, « Détroit venteux » (Windy Strait), en compte huit. Les mers suivantes apparaissent sous forme de cartes verrouillées.
- **La boucle :** carte, fiche de niveau, bataille, résultat avec une à trois étoiles, niveau suivant.
- **Déblocage :** réussissez un niveau et le suivant s'ouvre. Battez le boss et la mer suivante s'ouvre. Les étoiles ne bloquent jamais la progression ; ce sont des objectifs supplémentaires.
- **Son :** synthétisé dans le navigateur, avec une gamme pentatonique différente pour chaque mer et une note qui monte à chaque capture d'une chaîne.
- **La progression** est enregistrée dans le stockage local du navigateur, et le jeu fonctionne encore en mémoire si le stockage est bloqué.

## Comment il est construit

- **Un seul fichier.** Environ 95 Ko, sans requête externe ni police web, il fonctionne donc hors ligne et dans un cadre intégré.
- **Le moteur et l'écran sont séparés.** Le moteur est un module pur, sans DOM, sans horloge et sans appel aléatoire. L'interface se contente de mettre en file des commandes comme « envoyer 50 % de l'île 0 vers l'île 1 », et une boucle fait avancer le moteur toutes les 100 ms.
- **L'accélération consiste à avancer plus vite**, pas à changer les règles, si bien que les limites de temps des étoiles restent équitables à 2x.
- **La pause** arrête les ticks, et le jeu se met en pause tout seul quand l'onglet est masqué.

Garder le moteur pur était un pari sur l'avenir : le même code pourra plus tard tourner au tour par tour sur un réseau, et une liste de commandes enregistrée permet de rejouer une partie.

## Ce que nous avons testé

Nous avons piloté le prototype avec un Chrome sans interface. Sur un écran de 375 par 812, il est parti d'un stockage vide, a envoyé des flottes par glissement à la souris et par glissement tactile, a mis en pause (le compteur de ticks est resté figé), a gagné le niveau 1-1 en environ 12 secondes avec trois étoiles, a enregistré la progression, a débloqué le 1-2 et a conservé la progression après un rechargement. À 320 par 568, rien ne débordait sur les côtés. La console du navigateur n'a affiché aucune erreur.

Nous avons aussi fait une vérification déterministe : la même carte et les mêmes commandes ont donné le même résultat à chaque exécution, et une exécution en temps réel et une exécution au tour par tour ont abouti au même résultat.

## Ce que nous n'avons pas pu tester

- **Appareils réels.** iOS Safari et un téléphone Android milieu de gamme **ne sont pas vérifiés**. L'émulation tactile d'un navigateur sans interface n'est pas un doigt.
- **Performances.** Notre cible est de 22 îles et 300 flottes à 60 images par seconde. Cela n'a pas été mesuré.
- **Fonctions manquantes :** un mode de jeu libre, un moyen d'exporter les journaux de jeu, la sauvegarde en cours de niveau et plusieurs animations.
- **Défauts connus :** l'étiquette du glissement peut recouvrir le nombre d'une île voisine, et la fiche de niveau peut recouvrir des nœuds de la carte.

Les prochaines étapes sont un test de 30 minutes avec cinq à huit personnes, avec un journal de jeu intégré au préalable. Le prochain article porte sur le travail d'équilibrage que nous avons fait sans humains.
