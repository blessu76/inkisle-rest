---
title: Garder deux appareils au même pas : déplacer la synchronisation iCloud vers un kit d'application partagé
description: La progression, l'encre et les réglages d'Inkisle étaient déjà alignés entre appareils via iCloud. Le 16 novembre, nous avons déplacé ce pont vers un kit d'application partagé. Comment nous avons gardé les données sauvegardées intactes, les règles de fusion qui ne réduisent jamais, comment la marque d'achat est traitée et ce que nous n'avons pas vérifié sur de vrais appareils.
slug: keeping-two-devices-in-step
lang: fr
translation_of: en
category: making-of
keywords: Inkisle, iCloud, synchronisation entre appareils, données de sauvegarde, fusion, jeu mobile
image_alt: Deux écrans de tailles différentes reliés par un fil mince, avec les îles des deux cartes peintes des mêmes couleurs.
---

Dans Inkisle, notre jeu de stratégie de conquête d'îles pour iOS, la progression, l'encre et les réglages clés (langue et pseudo) sont alignés entre les appareils d'un même identifiant Apple grâce au stockage clé-valeur iCloud du joueur lui-même. Cette synchronisation existait déjà. Ce que nous avons fait le 16 novembre n'a pas été de la construire, mais de déplacer vers un kit d'application partagé un pont que nous avions écrit nous-mêmes, et la plus grande crainte était de ne perdre aucune valeur sauvegardée. Nous n'avons pas encore vérifié un aller-retour entre un vrai iPhone et un iPad [non vérifié]. Le jeu est en développement et n'est pas sorti.

## Ce que nous avons déplacé

La consigne du responsable ce jour-là était que la synchronisation des données de jeu entre appareils Apple soit obligatoire et qu'elle aille dans le kit d'application partagé. Nous avons trouvé le droit clé-valeur iCloud déjà activé, ainsi qu'un pont Swift et une enveloppe de stockage maison dans l'application. Donc :

| Élément | Ce qui a changé |
|---|---|
| Pont | Suppression de notre pont Swift et de l'enveloppe, et passage au stockage de plateforme du kit : iCloud sur iOS, local uniquement ailleurs |
| Clés et encodage | Clés de stockage, encodage des chaînes et identifiant de stockage laissés tels quels |
| Avant la lecture | Sur iOS, réveiller la synchronisation une fois juste avant une lecture (la synchronisation continue en cas d'échec) |
| Réglages du projet | Ajout de la capacité iCloud au fichier du projet également |

## Ne pas perdre de données

Comme les clés et les formats sont restés les mêmes, la nouvelle version lit ce qu'a écrit l'ancienne, et l'ancienne lit ce qu'écrit la nouvelle. Nous avons verrouillé les deux sens par des tests : lire un bloc d'ancien format avec le nouveau code, lire un nouveau bloc avec l'ancien code et lire un ancien bloc de réglages. Seul du code a été supprimé ; les valeurs sauvegardées n'ont pas été touchées.

## La fusion ne réduit jamais

Quand deux appareils ont une progression différente, nous avons gardé la fusion propre à l'application. Le kit a aussi un outil de fusion, mais nous ne l'avons pas utilisé. La fusion de l'application ne fait déjà que croître, et garder les mêmes clés et le même format était plus sûr en la laissant telle quelle.

- Les étoiles et les meilleurs records par étape prennent la valeur la plus grande.
- La progression retient l'appareil allé le plus loin, et l'encre et les réglages ne font que se combiner, sans jamais diminuer.
- Si la valeur dans le cloud diffère de ce que nous avons envoyé en dernier, nous l'envoyons de nouveau, afin de nous rattraper après une ancienne version qui a écrasé la même clé.

## Ce qu'est devenue la marque d'achat

Un article précédent disait que le déblocage ne passe pas sur un autre appareil. Ce travail l'a changé. Le bloc de synchronisation porte désormais une marque indiquant que Débloquer toutes les mers a été acheté, et un autre appareil qui la lit s'ouvre aussi. La marque **ne fait que croître.** Un bloc qui n'en contient pas ne la retire pas ; nous l'envoyons de nouveau.

C'est un changement de conception faisant suite à la consigne de « synchronisation obligatoire » du responsable, et il a une limite : une fois la marque synchronisée, un remboursement ne la retire pas sur les autres appareils. Le traitement des remboursements reste une décision de politique. Le parcours d'achat lui-même n'a pas non plus été exécuté sur un vrai appareil [non vérifié].

## Taille et tests

Le stockage clé-valeur iCloud a une limite totale (1 Mo). Le bloc de synchronisation d'une sauvegarde avec les 240 étapes terminées fait environ 6,3 Ko, et un test le maintient sous 16 Ko. Les 14 nouveaux tests couvrent des clés et un encodage inchangés, la fusion de deux appareils, la marque d'achat qui se propage sans jamais être retirée, le maintien en local hors ligne ou déconnecté, et la fusion après le retour en ligne. Sur les quatre fichiers de tests cloud, 77 tests ont réussi.

## Ce que nous n'avons pas vérifié

- **Une vraie synchronisation entre un iPhone et un iPad n'a pas été vérifiée [non vérifié].** On ne peut la voir que sur de vrais appareils ou via TestFlight.
- Les suppressions ne se propagent pas aux autres appareils, car cette synchronisation ne fait que fusionner.
- Android n'est pas concerné. Les données restent sur l'appareil.
- Si une ancienne version sur un autre appareil écrase la même clé, la marque d'achat peut brièvement disparaître, et la nouvelle version l'envoie de nouveau.
- La politique de confidentialité décrit désormais cette synchronisation : les données de jeu sont conservées dans l'iCloud du joueur, pas sur nos serveurs, et peuvent être désactivées dans les réglages de l'appareil.

## FAQ

### La progression d'Inkisle est-elle stockée sur un serveur ?

Non. Elle est alignée entre les appareils d'un même identifiant Apple grâce au stockage clé-valeur iCloud du joueur lui-même, et n'est pas envoyée à nos serveurs.

### La synchronisation peut-elle être désactivée ?

Oui. Désactiver iCloud pour cette application dans les réglages iOS arrête la synchronisation et laisse les données uniquement sur l'appareil.

### La synchronisation fonctionne-t-elle sur Android ?

Non. Sur Android, les données restent sur l'appareil.
