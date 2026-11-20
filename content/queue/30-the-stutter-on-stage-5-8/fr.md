---
title: La saccade du niveau 5-8 : c'était l'écran, pas le moteur du jeu
description: Le niveau 5-8 d'Inkisle saccadait. Nous avons mesuré avant de toucher à quoi que ce soit, constaté que le coût venait du dessin de l'écran et non des règles du jeu, et fait passer le coût d'une image de 3,4 à 1,3 ms sur un ordinateur. Ce que nous avons changé, ce que nous avons laissé et ce que nous n'avons pas vérifié sur téléphone.
slug: the-stutter-on-stage-5-8
lang: fr
translation_of: en
category: making-of
keywords: Inkisle, performance, saccade, temps d'image, conception de jeu, jeu mobile, optimisation
image_alt: Quatre grandes barres violettes à gauche et quatre petites barres corail à droite, avec une flèche entre elles et une ligne en pointillés qui marque le budget.
---

Inkisle, notre jeu de stratégie de conquête d'îles pour iOS, saccadait au niveau 5-8 pendant les tests. L'hypothèse facile était que le moteur du jeu, la partie qui déplace les flottes et décide des captures, était devenu trop lourd. Nous avons d'abord mesuré. Le problème n'était pas le moteur, mais l'écran qui l'entoure. Après le changement, le coût d'une image au niveau 5-8 est passé de 3,4 ms à 1,3 ms sur notre ordinateur. Le jeu est en développement et n'est pas sorti, et ces chiffres ne viennent pas d'un téléphone.

## Ce que nous avons mesuré

Une image comporte deux sortes de travail : faire avancer les règles du jeu d'un tick, et construire puis dessiner l'écran. Au niveau 5-8, un tick des règles ne coûtait en moyenne que 3 à 5 microsecondes. L'écran coûtait environ mille fois plus.

La plus grande part de ce coût d'écran venait de trois choses :

1. **Tout l'affichage tête haute était reconstruit à chaque image.** Le contrôleur du jeu annonçait un changement à chaque image, de sorte que les barres de puissance, le texte d'objectif, la feuille de résultats, la barre de proportion, les badges, la barre de choix, la couche de crise et le bouton de marée étaient tous reconstruits, même quand rien n'avait changé. Environ 2,5 ms sur 3,4 ms partaient dans la construction des widgets.
2. **Les étiquettes de nombres manquaient le cache.** La clé du cache comprenait la transparence et la taille exactes de chaque nombre, qui changent continuellement pendant l'expansion d'une capture ou un fondu. Chaque image produisait donc de nouvelles mises en page, et quand le cache dépassait 600 entrées, il était vidé d'un coup, si bien qu'une image devait tout remettre en page. Le temps de dessin sur le 1 % d'images les plus lentes valait de 5 à 10 fois la moyenne.
3. **De petites tâches répétées.** Chaque flotte cherchait deux fois sa couleur d'encre, la position et le rayon de chaque île étaient recalculés pour chaque flotte, et un cache de shader utilisait une clé de texte.

## Ce que nous avons changé

- L'affichage tête haute écoute désormais un petit signal qui ne se déclenche que lorsque quelque chose qu'il affiche change, comme le tick, la pause, la vitesse, l'état de crise, les objectifs ou les indices. Le dessin se fait toujours à chaque image, comme avant.
- Les étiquettes de nombres sont arrondies à des paliers grossiers (transparence en 32 paliers, taille au quart de pixel) pour que le cache soit atteint, et quand il est plein, seule la moitié la plus ancienne est retirée.
- Les recherches répétées sont calculées une fois par image, et la clé du shader est passée d'une chaîne à un enregistrement.

L'arrondi de la taille et de la transparence n'est pas visible à l'œil.

## Les chiffres

Ils ont été mesurés sur un ordinateur, avec un écran de 375 × 667, dans un mode qui ne sert qu'à comparer l'avant et l'après.

| | avant | après |
|---|---|---|
| Niveau 5-8, image entière, moyenne | 3 433 µs | 1 267 µs |
| Niveau 5-8, image entière, 1 % le plus lent | 10 803 µs | 5 182 µs |
| Niveau 5-8, dessin, moyenne | 818 µs | 201 µs |
| Niveau 5-8, dessin, 1 % le plus lent | 4 540 µs | 1 284 µs |

Un jeu à 60 images par seconde dispose d'environ 16,6 ms par image, donc même avant le changement, le travail tenait dans ce budget sur un ordinateur. C'est pourquoi la saccade ressentie peut avoir aussi une autre cause (voir plus bas).

## Ce que nous avons laissé tel quel

Nous n'avons pas modifié une seule ligne des règles ni du code d'équilibrage. Seule la couche d'écran a changé : la façon dont le contrôleur annonce les mises à jour, les widgets qui écoutent et les caches de dessin. La même graine produit toujours le même résultat de 600 ticks, et les vérifications existantes d'images de référence, de jeu déterministe et de simulations de bots sont restées au vert.

Nous avons aussi laissé un vrai coût pour plus tard. La prévision de crise s'exécute sur le fil de l'écran : sur le niveau le plus lourd que nous ayons mesuré, le 17-3, elle a pris en moyenne 3,4 ms et son 1 % le plus lent a atteint 11,8 ms, ce qui peut provoquer une petite saccade toutes les demi-secondes. Répartir ce travail sur plusieurs images donnerait le même résultat, mais risque de changer des décisions, donc nous ne l'avons pas fait maintenant. Au niveau 5-8, elle coûte 0,17 ms et cela n'a pas d'importance.

## Ce que nous avons ajouté

Un benchmark du moteur sans écran, et un test de performance avec des limites supérieures larges. Il attrape le genre de régression où le coût explose avec le nombre de flottes ou où chaque image alloue trop de mémoire. Nous avons gardé ces limites larges exprès, car des limites serrées échoueraient chaque fois que la machine de test est occupée. Par défaut, les plus lourds de ces tests sont ignorés et ne s'exécutent que sur demande.

## Ce que nous n'avons pas vérifié

- **Le débit d'images sur un vrai téléphone, à 60 ou 120 images par seconde, n'est pas vérifié.** Nos chiffres sont un coût de fil d'écran sur un ordinateur, pas un coût graphique sur un appareil.
- **Le voile de brouillard et les couches de bande ne sont ni mesurés ni modifiés.** Ils sont dessinés avec un flou plein écran, qui coûte à la puce graphique plutôt qu'au processeur. Si le niveau 5-8 saccade encore sur un téléphone, c'est notre premier suspect.
- Nous n'avons pas regardé le rendu dans un navigateur à 320, 375, 768 et 1280 px, car aucune mise en page n'a changé.
- Que la saisie paraisse plus réactive n'est qu'une attente de notre part.

## FAQ

### Pourquoi le niveau 5-8 d'Inkisle saccadait-il ?

Notre mesure désignait l'écran reconstruit et les étiquettes de nombres remises en page à chaque image, pas les règles du jeu. Nous avons corrigé cela ; le débit d'images sur un vrai téléphone n'est pas encore vérifié.

### L'optimisation a-t-elle changé la façon de jouer ?

Non. Nous n'avons pas touché aux règles ni au code d'équilibrage, et la même graine donne le même résultat qu'avant.

### Cela saccade-t-il encore sur un téléphone ?

Nous ne le savons pas encore. Nos chiffres viennent d'un ordinateur. Nous vérifierons sur un appareil réel dans TestFlight.
