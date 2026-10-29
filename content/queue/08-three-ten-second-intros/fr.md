---
title: Une intro de dix secondes en trois versions : ciel, mer et terre
description: Inkisle s'ouvre sur une intro de dix secondes qui existe en trois versions. Comment les trois partagent une même fin, pourquoi un sac mélangé décide de celle que vous voyez, quand elle se réduit à trois secondes, et ce qui se passe quand la réduction des animations est activée.
slug: three-ten-second-intros
lang: fr
translation_of: en
category: making-of
keywords: Inkisle, intro de jeu, lancement de l'appli, bouton passer, réduire les animations, accessibilité, jeu mobile
image_alt: Des îles dans une mer vert menthe, avec de l'encre couleur corail qui s'étale sur l'une d'elles, l'image d'ouverture de l'intro d'Inkisle.
---
La première chose que vous voyez en ouvrant Inkisle est une intro. Nous voulions qu'elle ressemble à un petit événement les premières fois, puis qu'elle **s'efface** ensuite. Cet article décrit comment l'intro est construite et les règles qui décident de ce que vous voyez.

## Une seule fin, trois débuts

L'intro complète dure **10 secondes**. Les 7 premières secondes existent en trois versions : **ciel**, **mer** et **terre**. Les 3 dernières secondes sont identiques dans toutes : la fin qui mène au menu. Partager la fin signifie que nous ne la dessinons qu'une fois, et que chaque version arrive au même endroit.

## Laquelle voyez-vous ?

Un choix au hasard peut montrer la même intro trois fois de suite, ce qui ressemble à un bug. L'appli utilise donc un **sac mélangé** : elle place les trois versions dans un sac dans un ordre aléatoire et en retire une à chaque lancement. Quand le sac est vide, il est rempli de nouveau. Deux conséquences :

- Au sein d'un même tour, **trois lancements de suite montrent les trois versions**.
- La première version d'un nouveau tour n'est jamais la même que la dernière que vous avez vue.

Le sac est enregistré sur le téléphone, il continue donc de fonctionner d'un lancement à l'autre.

## Longue d'abord, courte ensuite

Pour les **trois premiers lancements**, vous avez les 10 secondes complètes. À partir du quatrième lancement, l'appli ne joue que la fin commune, soit **3 secondes**. Un bouton « passer » apparaît **0,6 seconde** après le début de l'intro, pour qu'on ne demande pas à quelqu'un qui la découvre de la passer avant d'avoir rien vu. Passer appelle la même étape « terminé » que lorsque l'intro se finit, et un test vérifie qu'elle ne s'exécute qu'une seule fois.

## Réduire les animations

Si le réglage de réduction des animations du téléphone est activé (« Réduire les animations » sur iOS, ou animations désactivées sur Android), l'intro **ne bouge pas**. Elle affiche l'image finale de la fin pendant **1,2 seconde**, puis passe au menu. Le bouton « passer » est présent dès le début.

## Quand le sac enregistré est abîmé

Notre revue de code a montré qu'un sac enregistré abîmé n'était jamais réparé : l'appli n'arrivait pas à le lire, repartait de zéro à chaque lancement et continuait à montrer la version complète de 10 secondes. Le correctif consiste à traiter les données illisibles comme « aucune donnée » et à en écrire aussitôt de nouvelles. Si le stockage n'est pas du tout disponible, l'appli choisit une version au hasard et joue l'intro complète, et ne bloque jamais le démarrage du jeu. Des tests couvrent ces cas.

## Ce que nous n'avons pas vérifié

- Nous n'avons pas mesuré le comportement de l'intro sur un **vrai téléphone**. Les tests couvrent les règles ci-dessus, pas la fluidité de l'animation.
- Savoir si dix secondes est la bonne durée pour un premier lancement reste une supposition tant que d'autres personnes ne l'ont pas vue.
