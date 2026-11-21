---
title: Passer un niveau après trois défaites : une proposition douce, avec un coût
description: Dans Inkisle, après trois défaites sur le même niveau, le jeu propose de le passer pour 3 Ink. Quand il le propose, quels niveaux sont exclus, comment il apparaît sur la carte et comment c'est enregistré.
slug: skip-a-stage-after-three-losses
lang: fr
translation_of: en
category: making-of
keywords: Inkisle, passer un niveau, difficulté, game design, données de sauvegarde, jeu mobile
image_alt: Une carte marine avec une île portant un petit drapeau corail et un chemin en pointillés qui la contourne vers l'île suivante.
published: 2026-11-21T12:30+09:00
---

Dans Inkisle, notre jeu de stratégie de conquête d'îles pour iOS, perdre trois fois le même niveau fait apparaître la question : « Passer ce niveau et réessayer plus tard ? » Passer coûte 3 Ink. Le niveau passé reçoit un drapeau sur la carte et reste jouable à tout moment. Le jeu est encore en développement et n'est pas sorti ; nous n'avons pas encore vu cette fenêtre sur un vrai appareil.

## Pourquoi proposer de passer

Même après le réglage de la difficulté, certains niveaux restent particulièrement durs. Nous ne voulions pas qu'un joueur s'arrête sur une île. La proposition lui permet d'avancer et de revenir, plutôt que d'abandonner le jeu.

## Quand elle apparaît

- Juste après la **troisième défaite** sur le même niveau, une fois la feuille de résultat posée (1,1 seconde).
- Si le joueur refuse, elle ne revient pas aux 4e et 5e défaites, mais aux **6e, 9e** et ainsi de suite. Demander à chaque fois serait lourd ; ne demander qu'une fois laisserait de côté celui qui bloque encore.
- Les défaites sont comptées par niveau. Une victoire remet le compte à 0. Les défaites sur un niveau déjà réussi ou passé ne comptent pas.

## Ce que ça coûte

Passer coûte **3 Ink**, le même Ink que le joueur gagne dans le jeu ou achète. Aucune nouvelle monnaie, aucun nouveau produit. La valeur est une seule constante dans le code ; le texte, le bouton et le lien vers la boutique la suivent.

Nous avions d'abord mis 1 Ink, puis 3 après la demande du propriétaire de passer à 2 ou 3. Avec moins de 3 Ink, le bouton devient « Plus d'Ink, ouvrir la boutique » et ouvre la feuille de boutique existante. À partir de 3 Ink, le bouton pour passer revient.

## Niveaux exclus

- 1-1 à 1-4 : le tutoriel sans Ink. Passer là, ce serait ne jamais apprendre les commandes.
- 1-5 : le niveau où le jeu offre le premier Ink.
- Le dernier niveau : il n'y a pas de niveau suivant à ouvrir.
- Les niveaux de boss sont inclus.

## Ce que signifie un niveau passé

- Le niveau suivant s'ouvre et le niveau passé a **0 étoile**. Passer n'est pas réussir : on ne peut pas acheter d'étoiles.
- Sur la carte, le nœud reçoit un drapeau corail ; les lecteurs d'écran ajoutent « passé ».
- Si on le réussit plus tard, le drapeau disparaît et les étoiles sont enregistrées normalement.
- Une mer n'est terminée que par des niveaux réussis : il faut donc gagner le niveau au drapeau.
- La fin ne s'ouvre qu'avec une vraie victoire ; passer le 10-8 ne l'ouvre pas.

## Comment c'est enregistré

Le fichier de progression existant reçoit deux clés facultatives : le nombre d'échecs par niveau et la liste des niveaux passés. Si les deux sont vides, elles ne sont pas écrites, et une ancienne sauvegarde reste identique octet pour octet. À la lecture, les identifiants inconnus, les valeurs négatives et les textes sont écartés, et un niveau déjà réussi perd sa marque « passé », car la réussite l'emporte.

Pour la fusion iCloud, on garde le plus grand nombre d'échecs, on réunit les listes de niveaux passés, et une réussite sur un autre appareil l'emporte. Fusionner à nouveau le même instantané ne change rien ; un test le vérifie.

## Ce que nous n'avons pas vérifié

- La fenêtre et le drapeau sur un vrai appareil ou simulateur. Des tests de widgets en largeur 375 et 320 n'ont montré aucun débordement dans 16 colonnes de langue, mais nous n'avons pas regardé de captures.
- Si une ancienne version de l'app qui écrase l'instantané iCloud perd les deux nouvelles clés. Les niveaux réussis et les étoiles resteraient ; nous pensons que seule la marque serait perdue.
- Les traductions autres que le coréen et l'anglais n'ont pas été relues par des locuteurs natifs.

## Questions fréquentes

### Quand Inkisle propose-t-il de passer un niveau ?

Après trois défaites sur le même niveau, puis à la 6e, la 9e et ainsi de suite si on continue. Le début du jeu, le niveau cadeau 1-5 et le dernier niveau sont exclus.

### Combien ça coûte, et a-t-on des étoiles ?

3 Ink. Un niveau passé donne 0 étoile ; si on le réussit plus tard, on les reçoit comme d'habitude.

### Passer termine-t-il une mer ou ouvre-t-il la fin ?

Non. Une mer n'est terminée que par des niveaux réussis, et la fin ne s'ouvre qu'avec une vraie victoire.
