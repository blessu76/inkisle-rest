---
title: Envoyer depuis plusieurs îles à la fois: trois réécritures d'une seule commande
description: Attaquer une île depuis plusieurs des vôtres était la commande la plus difficile d'Inkisle. La première version par glissement, le correctif par sélection au toucher et la version par balayage, et ce que chacune nous a appris.
slug: three-rewrites-of-multi-island-attack
lang: fr
translation_of: en
category: making-of
keywords: Inkisle, commandes tactiles, UX de jeu mobile, sélection multiple, glisser-déposer, game design, itération
image_alt: Une bataille où plusieurs îles envoient des flottes vers une île ennemie.
---
Envoyer une flotte est facile : on glisse depuis son île vers la cible. Ce qui est difficile dans les commandes d'Inkisle, c'est **d'envoyer depuis plusieurs îles à la fois**, car les derniers niveaux se gagnent en arrivant ensemble. Nous avons réécrit cette commande trois fois en quelques heures, et l'histoire montre pourquoi.

## v0.1 : tout à la fois

Le premier prototype permettait plusieurs façons de faire :

- Glisser depuis une île vers une cible, et **passer sur vos autres îles en chemin** pour les ajouter comme sources.
- **Appui long** (0,4 seconde) sur une île pour sélectionner toutes les vôtres, puis glisser pour une attaque générale.
- Toucher une source, puis toucher la cible, comme alternative au glissement.

Sur le papier, cela couvrait tout. En pratique, un pouce recouvre justement l'île qu'il survole, et un niveau qui enseignait « passez sur les îles en glissant » demandait un geste difficile à voir et difficile à viser.

## v0.1.1 : sélectionner d'abord, puis partir

Le correctif a consisté à diviser le geste en deux. **Touchez vos îles une par une pour les sélectionner**, puis touchez la cible et elles partent toutes. Glisser une île sélectionnée envoie toujours tout le groupe. Nous avons ajouté :

- un petit badge au-dessus de la sélection qui indique combien d'îles sont choisies,
- un toucher sur la mer vide pour effacer la sélection,
- une zone de sélection plus large lors de l'ajout en glissant (rayon de l'île plus 12 px), car un doigt est plus gros qu'une île,
- une astuce affichée les premières fois, et les cartes de niveau qui enseignent la commande décrivent désormais le toucher.

Toucher est précis et paisible, mais avec beaucoup d'îles, cela fait **beaucoup de touchers** avant chaque attaque. Dans un jeu en temps réel, c'est du temps.

## v0.1.2 : balayer pour choisir

La version la plus récente permet de **balayer vos îles du doigt pour les choisir d'un seul trait**, puis de choisir la cible. Sélectionner quatre îles devient un seul mouvement au lieu de quatre touchers. Savoir si les méthodes précédentes restent disponibles en secours, et quelle sensation procure le balayage dans le détail, n'est pas définitif **[non vérifié au moment de la rédaction]**.

## Ce que nous avons appris, et ce que nous ne savons pas

- **Un geste qui demande au doigt de se poser sur une petite cible en mouvement est fragile sur un téléphone.** Le premier correctif a supprimé la visée ; le second a supprimé la répétition.
- Chaque version a réglé un problème et révélé le suivant, ce qui est normal, mais cela signifie aussi que la commande n'est pas encore stabilisée.
- Nous n'avons **aucune donnée de joueurs extérieurs** sur aucune des trois versions. La sensation exacte de la v0.1.2 est **[non vérifiée]** tant que d'autres ne l'ont pas essayée.

Le test avec cinq à huit personnes est le moment où cette commande sera vraiment jugée. S'ils hésitent encore avant d'attaquer, nous la changerons une quatrième fois.
