---
title: Régler la difficulté avec des bots: cinq niveaux qui étaient faux
description: Nous avons joué chaque niveau avec des bots simples sur 40 graines par niveau, et trouvé des niveaux impossibles, trop courts ou trop difficiles. Les cinq changements, les taux de victoire avant et après, et pourquoi les bots ne sont pas des humains.
slug: tuning-the-difficulty
lang: fr
translation_of: en
category: making-of
keywords: Inkisle, équilibrage de jeu, réglage de la difficulté, simulation de bots, taux de victoire, level design
image_alt: Une bataille animée entre plusieurs camps de couleurs différentes dans le prototype d'Inkisle.
---
Nous n'avons pas encore de testeurs, alors nous avons posé une autre question : quels niveaux sont *manifestement* faux ? Deux bots simples ont joué chaque niveau 40 fois, avec 40 graines différentes, et nous avons lu les taux de victoire.

## Les deux bots

- **Bot simple :** tous les 10 ticks, il attaque l'île la moins chère qu'il peut battre. Il représente un joueur occasionnel.
- **Bot expert :** tous les 5 ticks, il rassemble jusqu'à trois îles et attaque ensemble.

Aucun des deux n'est une personne. Ils nous donnent une direction, pas la difficulté telle qu'un humain la ressent.

## Cinq niveaux qui étaient faux

| Niveau | Problème | Changement | Bot simple avant → après |
|---|---|---|---|
| 1-1 | L'objectif trois étoiles « perdre 5 au maximum » était impossible : les îles neutres seules coûtaient 13 | Objectif changé en « 14 au maximum » | Trois étoiles 0 % → 100 % |
| 1-5 | Terminé en 18 secondes | Base ennemie 20 → 26, une île neutre donnée à l'ennemi | 100 %, maintenant 30 s |
| 1-8 boss | Pratiquement impossible à battre | Deuxième île de l'ennemi rendue plus petite, île au drapeau 24 → 26, une petite île donnée au joueur | **0 % → 53 %** |
| 2-2 | Terminé en 23 secondes | Base du joueur 15 → 20, une île donnée à l'ennemi | 100 %, maintenant 38 s |
| 2-8 boss | Trop difficile | Île au drapeau 24 → 28, une forteresse ennemie transformée en forteresse neutre de 14 | **10 % → 38 %** |

Nous avons laissé les 11 autres niveaux tels quels. La cible était un niveau de boss qu'un joueur occasionnel bat après environ un essai de plus, soit 40 à 60 % pour le bot simple.

## Effets secondaires remarqués

- Sur un jeu de 20 graines, le taux de victoire global du bot simple est passé de 84 % à 91 % et celui du bot expert de 78 % à 82 %.
- Le niveau 2-2 est devenu *plus difficile* pour le bot expert, de 100 % à 65 %. Nous pensons que le bot a l'habitude de vider les forteresses, mais cela reste **[non vérifié]**.
- Les niveaux 2-4 et 2-7 montrent de faibles taux de victoire pour le bot expert, 40 % et 38 %. Dans un combat chargé, rassembler ses forces pourrait nuire. Également **[non vérifié]**.
- Les limites de temps pour les deux étoiles semblent trop généreuses, puisque les bots les atteignent presque toujours. Nous les resserrerons quand nous verrons des temps humains.

![Trois écrans de téléphone montrant des combats animés dans le prototype. Le texte des captures est en coréen.](/assets/posts/img/tuning-boss.jpg)
*Des niveaux chargés du prototype : une mêlée au milieu de la mer, un niveau de boss avec l'île au drapeau encerclée, et un écran de 320 px de large.*

## Pourquoi les bots ne sont pas des humains

Un bot ne lit jamais mal un nombre, ne s'ennuie jamais et ne se trompe jamais en faisant glisser son doigt. Les 30 premières minutes d'une personne sont le vrai test : où elle réessaie, où elle abandonne, combien de temps elle met pour arriver à « suivant ». Le plan est d'ajouter d'abord un journal de partie, puis d'observer cinq à huit personnes. D'ici là, ces chiffres disent seulement qu'aucun niveau n'est clairement cassé, et c'est une affirmation plus faible que « la difficulté est bonne ».
