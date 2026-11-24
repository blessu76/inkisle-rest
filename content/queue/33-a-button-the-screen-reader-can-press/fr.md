---
title: Un bouton que le lecteur d’écran peut actionner
description: L’icône de fermeture et le phare d’Inkisle avaient des libellés lus à voix haute, mais il manquait leur action d’accessibilité. Nous avons vérifié les mots et ce qui se passe quand on active la commande.
slug: a-button-the-screen-reader-can-press
lang: fr
translation_of: en
category: making-of
keywords: Inkisle, accessibilité, lecteur d’écran, interface, tests de widgets
image_alt: Une croix et une icône de phare sur deux petites cartes, avec un contour de focus autour de chaque commande.
---

Inkisle est un jeu de stratégie et de conquête d’îles en développement. Lors d’un contrôle d’accessibilité, nous avons examiné la manière dont le jeu décrit ses commandes à un lecteur d’écran. Deux ont retenu notre attention : la croix qui ferme un panneau et le phare sur la carte qui permet de revoir une fin. Nous développons le jeu pour iOS.

## Du nom à l’action

Les deux commandes avaient déjà un nom. Dans l’arbre d’accessibilité de Flutter, le nœud qui portait ce nom avait perdu son action de pression quand nous avions remplacé la description par défaut de l’icône. Nous avons associé l’action au nœud qui porte le libellé. Dans les tests, activer Fermer referme le panneau et activer le phare ouvre la fin.

## L’entendre une fois

Nous avons aussi examiné ce qui était lu deux fois. Un bouton qui règle la proportion de flotte à envoyer exposait le même pourcentage dans son libellé et dans le texte visible. La commande pour passer l’intro et les repères numérotés de la carte présentaient des répétitions similaires. Dans chaque cas, nous avons gardé un seul libellé lu à voix haute, avec de quoi identifier la commande.

## Questions fréquentes (FAQ)

### Est-ce que cela a été testé avec un lecteur d’écran sur un téléphone ?

Les tests de widgets ont vérifié les libellés et les actions d’accessibilité. Nous n’avons pas encore vérifié les changements avec VoiceOver sur un iPhone.

### À quoi sert le phare sur la carte ?

Activez-le pour revoir une fin.
