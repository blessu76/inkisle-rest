---
title: Un son désactivé par défaut : une gamme pour chaque mer
description: Inkisle démarre en silence et c'est le joueur qui active le son. Comment les sons sont créés par le code sans fichiers audio, comment chaque mer a sa propre gamme de cinq notes, et pourquoi une chaîne de captures grimpe dans la gamme.
slug: sound-off-by-default
lang: fr
translation_of: en
category: making-of
keywords: Inkisle, audio de jeu, son procédural, gamme pentatonique, jeu mobile, accessibilité, réglages
image_alt: Cinq notes ascendantes dessinées comme de petits points d'encre au-dessus d'une rangée d'îles.
---
Beaucoup de gens jouent sur leur téléphone en public ou au lit. Un jeu qui démarre fort est un jeu qu'on ferme. C'est pourquoi, dans Inkisle, **le son est coupé tant que le joueur ne l'active pas**, et ce réglage est enregistré.

## Coupé, c'est vraiment coupé

Quand le son est désactivé, le code audio n'est même pas lancé : le lecteur de son est créé la première fois qu'un son est réellement nécessaire. Un jeu en sourdine ne touche jamais au système audio du téléphone. Si le réglage enregistré est abîmé ou si le stockage échoue, la réponse est de nouveau « désactivé ». L'appli respecte aussi le commutateur silencieux du téléphone. Les erreurs survenant dans le code audio sont interceptées au lieu de s'échapper, ce qui a été un correctif après qu'une revue de code a montré qu'un type d'erreur audio pouvait passer à travers le filet de sécurité.

## Aucun fichier son

Chaque son est **fabriqué par le code**. L'appli construit pour chaque tonalité un court WAV 16 bits mono à 22 050 échantillons par seconde : une onde (sinusoïdale, triangulaire ou en dents de scie), une attaque de 12 ms et une décroissance exponentielle. Il n'y a aucun fichier enregistré à licencier. Les paramètres des tons viennent du prototype web, l'appli sonne donc comme le prototype.

## Une gamme pour chaque mer

Chaque mer a sa propre **gamme pentatonique**, cinq notes qui sonnent bien dans n'importe quel ordre :

| Mer | Intervalles au-dessus de la note de base (demi-tons) |
|---|---|
| Baie calme (Calm Bay) | 0, 2, 4, 7, 9 |
| Détroit venteux (Windy Strait) | 0, 2, 5, 7, 9 |

La note de base est de 523,25 Hz. La deuxième mer ne diffère que d'une note, le troisième intervalle (5 au lieu de 4).

## Les chaînes grimpent

Quand vous capturez plusieurs îles à la suite, **chaque capture est une marche plus haut** dans la gamme de la mer. Après cinq marches, la gamme monte d'une octave, et au-dessus de la dixième marche elle reste sur la note la plus haute. Une belle chaîne s'entend donc comme une ligne ascendante, et comme la gamme ne contient que des notes qui s'accordent, une chaîne rapide reste juste.

## Ce que nous n'avons pas vérifié

- Les tests vérifient les notes et que « coupé » veut dire silence. Ils ne peuvent pas nous dire si **cela sonne bien**. Personne en dehors de l'équipe n'a écouté sur le haut-parleur d'un vrai téléphone ou au casque.
- Ces tons sont de simples bips. Qu'ils restent le son définitif ou soient remplacés n'est pas décidé.
