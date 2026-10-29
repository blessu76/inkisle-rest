---
title: Trois étoiles, une règle : comment un niveau est noté
description: Chaque niveau d'Inkisle peut rapporter jusqu'à trois étoiles. Ce que signifie chaque étoile, pourquoi les étoiles ne bloquent jamais la progression et ne baissent jamais, les 13 types d'objectifs trois étoiles et l'étiquette erronée que nous avons trouvée et corrigée.
slug: three-stars-one-rule
lang: fr
translation_of: en
category: making-of
keywords: Inkisle, notation par étoiles, progression du jeu, game design, jeu mobile, rejouabilité
image_alt: Une rangée de trois étoiles, les deux premières remplies de corail et la troisième seulement en contour.
---
Chacun des 16 niveaux d'Inkisle donne de une à trois étoiles. Les étoiles sont la façon qu'a le jeu de dire « vous pouvez faire mieux » sans vous y forcer. Voici la règle, et une erreur que nous avons faite en l'expliquant.

## Ce que signifie chaque étoile

1. **★1 : gagner.** Vous battez le niveau.
2. **★2 : gagner dans la limite de temps du niveau.** Chaque niveau a sa propre limite.
3. **★3 : l'objectif propre du niveau.** Un objectif différent pour chaque niveau, affiché sur sa carte.

Le jeu décide ces trois conditions à un seul endroit, et les écrans ne lui demandent que le résultat. Cela semble évident, mais quand nous avons écrit pour la première fois le graphique et la feuille de résultats, des morceaux de la règle s'étaient glissés dans les deux. Une revue l'a trouvé, et nous avons déplacé les vérifications dans de petites fonctions utilitaires à côté de la règle : si la règle change, il n'y a qu'un seul endroit à modifier.

## Les étoiles ne gênent jamais

- **Les étoiles ne débloquent rien.** Gagner un niveau ouvre le suivant. Battre le boss ouvre la mer suivante.
- **Les étoiles ne baissent jamais.** Rejouez un niveau et perdez : rien n'est enregistré. Rejouez et gagnez : le jeu garde le meilleur de tout, une étoile obtenue reste, et le meilleur temps est conservé.

Rejouer ne peut donc que vous aider.

## Treize types d'objectifs trois étoiles

L'objectif ★3 est différent dans presque tous les niveaux. Il y a 13 types pour l'instant, par exemple :

- perdre au plus un certain nombre de troupes,
- gagner sans jamais envoyer 100 %,
- prendre toutes les îles vides,
- ne perdre aucune île,
- capturer une forteresse en une seule attaque,
- repousser une fois une attaque ennemie simultanée,
- ne pas attaquer l'île mère de l'ennemi avant un temps donné.

Chaque objectif est écrit en mots simples dans l'appli, par exemple « Gagnez sans envoyer 100 %. »

## L'étiquette erronée

L'étiquette de ★1 disait d'abord « **gagner en gardant vos îles** ». Mais la condition était seulement « gagner » : on pouvait perdre des îles et obtenir quand même l'étoile. L'étiquette promettait quelque chose que le jeu ne vérifiait pas. Une revue l'a repéré, et l'étiquette est maintenant simplement « **gagner** ».

## Ce que nous n'avons pas vérifié

- Les limites de temps de ★2 ont été fixées par le prototype et, comme l'a montré le test avec des bots dans un article précédent, semblent **trop généreuses** pour les bots. Nous ne savons pas encore à quoi ressemblent les temps humains.
- Nous ne savons pas si les joueurs trouveront que 13 objectifs différents sont intéressants ou simplement déroutants.
