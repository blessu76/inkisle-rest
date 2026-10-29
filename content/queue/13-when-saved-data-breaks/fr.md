---
title: Quand les données sauvegardées se corrompent: comment l'appli récupère
description: Un téléphone peut perdre, tronquer ou bloquer les données sauvegardées d'une appli. Comment Inkisle gère un stockage absent, endommagé, obsolète ou indisponible pour la progression, l'intro et le réglage du son, et où notre récupération reste encore rudimentaire.
slug: when-saved-data-breaks
lang: fr
translation_of: en
category: making-of
keywords: Inkisle, données de sauvegarde, gestion des erreurs, robustesse, stockage local, jeu mobile, sauvegarde versionnée
image_alt: Un petit carnet dont une page est déchirée, à côté d'une rangée d'îles, une façon calme de représenter une sauvegarde endommagée.
---
Inkisle n'a ni comptes ni serveur, donc toute la progression vit **uniquement sur le téléphone**. Cela rend les données sauvegardées simples, mais cela signifie aussi que personne ne peut les restaurer à votre place. La question que nous nous sommes posée : que doit faire l'appli quand ce qu'elle relit est faux ?

## Quatre choses qui peuvent mal tourner

| Situation | Ce que fait l'appli |
|---|---|
| Rien n'est encore sauvegardé | Commencer au niveau 1-1 |
| Le texte sauvegardé est endommagé (illisible) | Le traiter comme vide, repartir de zéro |
| Sauvegardé par une autre version du format | L'ignorer, repartir de zéro |
| Le stockage du téléphone ne peut pas être ouvert du tout | Jouer en mémoire ; rien ne casse, mais rien n'est conservé à la fermeture |

Les données sauvegardées portent un numéro de version dans leur nom et dans leur contenu, de sorte qu'un futur changement de format puisse être reconnu au lieu d'être mal lu.

## Un dommage à un endroit n'efface pas le reste

Le fichier de progression contient une entrée par niveau. Notre relecture a relevé qu'une seule entrée endommagée réinitialisait autrefois tout. Désormais, chaque niveau est lu séparément : une entrée illisible est ignorée et les autres niveaux sont conservés. Seul un fichier totalement illisible, ou une version différente, entraîne un nouveau départ. Les entrées doivent aussi indiquer que le niveau a été **gagné**, car seules les victoires sont écrites.

## Une réparation qui répare vraiment

L'intro conserve sa propre petite sauvegarde (le sac mélangé d'un article précédent). Quand elle était endommagée, la lecture échouait avant que l'appli n'écrive quoi que ce soit de nouveau, si bien que le texte cassé restait là et que le problème se répétait à chaque lancement. Le correctif : si la lecture échoue, on repart de la valeur par défaut et on **écrit cette valeur par défaut par-dessus**. Le code de l'intro a des tests pour les sauvegardes cassées.

## Les réglages reviennent au choix silencieux

Le seul réglage est le son. Si ses données sauvegardées sont cassées, la réponse est **désactivé**, pas activé. Un fichier cassé ne devrait jamais rendre le jeu plus bruyant.

## La progression ne peut que croître

Les étoiles et les meilleurs temps ne font que s'améliorer, et une rejouée perdue ne change rien. La règle de déverrouillage regarde uniquement si le niveau précédent a été gagné.

## Ce que nous n'avons pas vérifié

- Nous avons testé dans le code le texte endommagé, les mauvaises versions et le stockage absent. Nous n'avons **pas** testé un téléphone sans espace libre ni une sauvegarde et restauration du système d'exploitation.
- Quand tout le fichier est illisible, le joueur recommence au niveau 1-1. Pour un joueur qui a beaucoup d'étoiles, ce serait pénible, et nous n'avons pas décidé d'ajouter quelque chose de plus doux.
