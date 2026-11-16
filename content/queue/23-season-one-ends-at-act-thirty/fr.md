---
title: De 100 actes à 30, et une fin qui reste ouverte : la fin de la saison 1
description: Le premier plan comptait 100 actes et 800 étapes. Pourquoi nous avons clos la saison 1 à 30 actes et 240 étapes, comment nous avons gardé le plan à 100 actes comme candidat au lieu de l'abandonner, et comment la fin sans mot de conclusion a été conçue.
slug: season-one-ends-at-act-thirty
lang: fr
translation_of: en
category: making-of
keywords: Inkisle, saison 1, 30 actes, fin, fin ouverte, game design, jeu mobile
image_alt: Une longue route maritime sur une carte qui s'arrête avant une mer calme, avec une petite lumière allumée sur la dernière île.
---

La saison 1 d'Inkisle, notre jeu de stratégie de conquête d'îles pour iOS, se termine à l'acte 30 avec 8 étapes par acte, soit 240 étapes au total. Le premier plan comptait 100 actes et 800 étapes ; nous avons gardé ce plan comme candidat pour une saison 2 au lieu de l'abandonner. La fin de l'acte 30 tient en trois scènes de moins de 30 secondes et ne dit jamais « the end ». Le jeu est encore en développement et n'est pas sorti.

## Pourquoi nous l'avons réduit

Le premier objectif était 100 actes × 8 étapes = 800 étapes. C'est pourquoi certains articles précédents, sur la courbe de difficulté et l'itinéraire de la carte, sont écrits en pensant à 800 étapes. Le 15 novembre, le responsable a changé la décision : **la saison 1 se termine à l'acte 30, avec une fin affichée après l'acte 30.**

La décision ne donne pas de longue justification. Elle indique seulement que, à ce moment-là, 23 actes étaient terminés et 77 restaient, et que la décision faisait des actes 27 à 30 plus la fin le travail restant pour la saison 1. Pourquoi exactement 30 reste [unverified] ; la structure donnée par les documents est que trois volumes de dix actes forment une histoire qui peut se clore.

## Le plan à 100 actes n'est pas jeté

Les volumes 4 et suivants (actes 31 à 100) sont conservés dans les documents comme « candidat saison 2 ». Les volumes 1 à 3 sont identiques à la saison 1, donc seul le volume 4 et suivants sert de matière candidate. **Rien n'a été décidé concernant une saison 2.** Si nous la faisons, nous recompterions d'abord les actes et déciderions comment la relier à la fin de l'acte 30.

## Trois volumes

| Volume | Actes | Thème |
|---|---|---|
| 1 | 1 à 10 | Les règles de base de la propagation de l'encre |
| 2 | 11 à 20 | Routes et flux (lignes de carte, marées) |
| 3 | 21 à 30 | Deux encres se rencontrent, des lignes effacées et des mains qui se joignent |

L'acte 26 est le sommet de l'histoire, et les actes 27 à 30 en descendent et convergent. Le boss de l'acte 30 utilise une nouvelle condition de victoire : tenir plus de la moitié des îles pendant 30 secondes avec une flotte alliée (et non prendre toutes les îles). L'objectif de taux de victoire du bot pour ce combat était de 32 %.

## La fin : pas de mot de conclusion

Nous avons pris deux décisions. La première est une **fin ouverte**. La dernière ligne est une traduction du coréen « The deep water reflects. », et il n'y a aucun « The end » dans aucune langue. La seconde est que l'écran de fin affiche « Inkisle · Season 1 ». Le texte de la boutique ne parle que de « 30 actes ».

- **Scène 1 :** quatre lignes de texte montent lentement au-dessus de l'encre qui se répand.
- **Scène 2 :** un voile de nuit tombe et le parcours apparaît en lettres dorées : mers traversées, étapes gagnées et étoiles collectées, comptées à partir de 0. Les chiffres sont calculés à partir de la sauvegarde.
- **Scène 3 :** la mer calme revient avec la dernière ligne, « Inkisle · Season 1 » et une ligne de remerciement.

L'ensemble dure moins de 30 secondes, et un toucher passe à la dernière image fixe. Une cloche sonne exactement une fois pendant la scène 3, et ne sonne pas si le joueur a passé la séquence, si la réduction des mouvements est activée ou si les effets sonores sont coupés. La fin ne se joue qu'une fois, automatiquement, la première fois que l'acte 30, étape 8, est terminé. Pour la revoir, le joueur touche le phare en haut de l'acte 30.

## Corriger le mot « dernier »

Si la saison se termine à l'acte 30, des mots antérieurs comme « dernier » ne conviennent plus. Nous avons trouvé trois lignes dans les actes 10 et 11 (« la dernière mer », « la fin de la carte ») et les avons remplacées par une formulation ouverte, par exemple « Au-delà, la carte ne contient encore rien. »

## Ce que nous n'avons pas vérifié

- Le fondu lent, l'aspect doré et le volume de la cloche **n'ont pas été vus sur un appareil réel [unverified].** Jusqu'ici, nous n'avons vérifié que des rendus en 375 px et 320 px dans des tests de widgets.
- Le texte de fin dans des langues autres que le coréen et l'anglais est traduit automatiquement et n'a pas été relu [unverified].
- Il n'existe pas de plan de saison 2 et aucune date de sortie n'a été fixée.

## FAQ

### Combien d'étapes compte la saison 1 d'Inkisle ?

30 actes de 8 étapes chacun, soit 240 étapes au total. Le jeu est encore en développement et n'est pas sorti.

### Avez-vous abandonné le plan de 100 actes et 800 étapes ?

Non. Le volume 4 et suivants est conservé comme candidat pour une saison 2, et nous n'avons pas décidé de faire une saison 2.

### Le jeu se termine-t-il quand la fin est jouée ?

Non. Rejouer les actes 1 à 30, collecter trois étoiles et les tableaux de scores continuent. La fin clôt l'histoire, pas l'application.
