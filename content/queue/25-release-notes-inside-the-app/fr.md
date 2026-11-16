---
title: Notes de version dans l'application : une feuille en 12 langues et un contrôle de longueur
description: Les notes de version d'Inkisle sont une feuille accessible depuis les Réglages, et non une page web. Comment les notes de chaque build sont rédigées en 12 langues, les contrôles du nombre d'éléments et de leur longueur, et le bug de test qui affichait une feuille vide.
slug: release-notes-inside-the-app
lang: fr
translation_of: en
category: making-of
keywords: Inkisle, notes de version, localisation, multilingue, tests, jeu mobile
image_alt: Une feuille de papier qui remonte du bas d'un écran, avec douze petits onglets de langue alignés au-dessus.
---

Les notes de version d'Inkisle, notre jeu de stratégie de conquête d'îles pour iOS, sont une feuille dans l'application, ouverte depuis les Réglages, et non une page web. Les notes de chaque build sont rédigées en 12 langues, et un script de contrôle vérifie le nombre d'éléments et leur longueur. Le contrôle du build 34 a donné 0 erreur et 0 avertissement. Le jeu est encore en développement et n'est pas sorti.

## Nous avons supprimé la page web

Au début, l'écran principal comportait un lien « Notes de version » et un bouton d'information (ⓘ). Dans le build 32, nous avons supprimé les deux. Le contenu de la fenêtre d'information (politique de confidentialité, conditions, version, licences open source, exploitant, contact et la mention 16+) a été déplacé dans les Réglages, et les notes de version sont devenues une feuille ouverte depuis une ligne « Notes de version » dans ces Réglages. La page des notes de version du site a également été retirée le 15 novembre. Sans site séparé, le texte de l'application est la seule source.

La feuille utilise le même cadre que nos autres fenêtres (InkSheet). Elle occupe au maximum 60 % de la hauteur de l'écran, la ligne du titre et la croix de fermeture (48×48) restent fixes, et seul le contenu défile à l'intérieur de la feuille.

## Un build, un fichier, 12 langues

Pour chaque build, `release_notes/<build>.json` contient un titre, une introduction et les éléments en 12 langues (ko, en, ja, zh-Hant, es, pt-BR, fr, de, id, th, vi, tr). Les fichiers sont regroupés dans `assets/release_notes.json`, livré avec l'application, et la feuille le lit.

## Contrôles de longueur et de nombre

Un script de contrôle lit les fichiers et signale les écarts aux règles.

- **RN06 :** un élément doit compter 200 caractères ou moins. Le texte allemand était trop long, si bien que l'élément de fin de saison du build 34 a été ramené à 183 caractères. Dans le build 31, nous avons séparé un élément d'achat en deux pour respecter la limite.
- **RN05 :** de 3 à 6 éléments sont recommandés. Il ne s'agit que d'un avertissement, qui ne bloque pas une sortie. Les avertissements restants concernent d'anciens builds comptant 1 ou 2 éléments ; ils témoignent fidèlement de ce qui avait été écrit, nous les avons donc laissés.
- Un test échoue s'il n'existe pas d'entrée pour la version et le numéro de build en cours, si bien que chaque montée de build exige que la note en 12 langues soit rédigée au préalable.
- Le script d'envoi iOS lance le contrôle des notes de version avant la porte verte (format, analyse, tests).

## Le test qui voyait une feuille vide

Deux tests de la feuille de notes de version ont commencé à voir une feuille vide. La cause venait du test, pas de l'application. Le bundle est un vrai fichier d'assets et, en grossissant, `pumpAndSettle`, qui attend que l'écran se stabilise, se terminait avant que la lecture du fichier ne soit achevée. Nous avons modifié les tests pour ouvrir la feuille, attendre 300 ms avec `runAsync`, puis redessiner. Le code de l'application n'a pas changé.

## Ce que nous n'avons pas vérifié

- Les traductions autres que le coréen et l'anglais sont faites par machine et n'ont pas été relues par des locuteurs natifs [non vérifié].
- Nous n'avons pas vu la feuille ouverte à 60 % sur un appareil réel. Des tests de widgets en 375×667 et 320×568 en tiennent lieu [non vérifié].

## Questions fréquentes

### Où trouver les notes de version d'Inkisle ?

Dans l'application, touchez la ligne « Notes de version » dans les Réglages : une feuille s'ouvre. Il n'existe pas de page web séparée. Le jeu n'est pas encore sorti.

### En combien de langues sont-elles rédigées ?

En 12 langues. Hormis le coréen et l'anglais, elles sont traduites automatiquement et n'ont pas encore été relues.

### Que se passe-t-il si un élément est trop long ?

Si un élément dépasse 200 caractères, le script de contrôle signale une erreur, et nous le raccourcissons ou le séparons en deux.
