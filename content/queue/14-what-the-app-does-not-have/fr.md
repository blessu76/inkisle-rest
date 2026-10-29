---
title: Ce que l'appli n'a pas: ni publicités, ni comptes, ni suivi
description: Une partie du design d'Inkisle consiste à ce qu'on a laissé de côté. L'appli ne demande pas de compte et n'a ni publicités ni outils de suivi, elle fonctionne sur iOS et Android à partir d'une seule base de code, et nous avons dessiné une nouvelle icône pour les deux. Ce que nous avons décidé et ce que nous n'avons pas vérifié.
slug: what-the-app-does-not-have
lang: fr
translation_of: en
category: making-of
keywords: Inkisle, confidentialité, sans publicité, sans compte, icône d'appli, iOS, Android, Flutter, jeu mobile
image_alt: Une île corail dessinée comme une simple tache d'encre sur fond crème, l'icône de l'appli Inkisle.
---
Une grande partie de ce qui rend une appli agréable tient à ce qu'elle **ne** fait **pas**. Pour la première version d'Inkisle, nous avons arrêté une courte liste de choses à laisser de côté.

## Pas de compte, pas de publicités, pas de suivi

- **Pas de compte.** Vous ouvrez l'appli et vous jouez. Il n'y a ni inscription ni connexion.
- **Pas de publicités ni d'outils de suivi.** La liste des paquets externes de l'appli est courte : un pour enregistrer de petits réglages sur le téléphone, un pour jouer des sons et un pour ouvrir une page web. Il n'y a aucun paquet publicitaire, aucun paquet d'analyse et aucun paquet de connexion.
- **La progression reste sur le téléphone.** Les étoiles sauvegardées et le réglage du son sont stockés localement et ne sont envoyés nulle part.

L'appli a un écran d'informations avec un lien vers la politique de confidentialité, qui est la même page que celle de ce site web. La seule chose qui touche le réseau est l'ouverture de cette page, et cela n'arrive que lorsque le joueur appuie dessus. La politique a d'abord été rédigée pour ce site web ; il faut donc encore la vérifier et la mettre à jour pour qu'elle couvre l'appli avant d'envoyer quoi que ce soit à une boutique.

## Une base de code, deux plateformes

Inkisle est construit avec Flutter, donc **iOS et Android sont développés ensemble** à partir du même code, et chaque modification est testée sur les deux. Le plan est de **sortir d'abord sur iOS**. Nous compilons et testons quand même Android en permanence, pour qu'il ne devienne pas un second projet plus tard. Le jeu est verrouillé en orientation portrait sur les deux. Les versions minimales sont iOS 13 et Android API niveau 24.

## L'icône

L'icône est une simple **île d'encre corail** sur un fond crème. Un seul code de dessin génère trois fichiers :

- l'icône carrée normale pour iOS et les anciens Android,
- le premier plan « adaptatif » d'Android, dessiné dans la zone de sécurité de 66 % sur laquelle Android recadre,
- une silhouette d'une seule couleur pour les icônes à thème d'Android 13.

Nous avons livré un bug ici et l'avons corrigé : l'icône adaptative était réduite deux fois (une fois par nous et une fois par les paramètres de compilation), si bien qu'elle paraissait trop petite sur Android. Maintenant la réduction n'a lieu qu'à un seul endroit.

## Ce que nous n'avons pas vérifié

- Nous n'avons pas fait tourner l'appli sur un **vrai iPhone ou téléphone Android** à partir d'une version de boutique, et nous ne l'avons soumise à aucune des deux boutiques. Des points comme la validation par les boutiques, les écrans de l'appli dans d'autres langues et l'aspect de l'icône sur différents lanceurs restent ouverts.
- « Pas de suivi » décrit ce qui se trouve dans notre propre code et notre liste de paquets. Nous n'avons pas audité les paquets dont nous dépendons au-delà de la lecture de leurs descriptions.
