---
title: Deux mers gratuites et un seul déblocage : comment nous avons simplifié le paiement
description: Inkisle garde les mers 1 et 2 gratuites et ouvre le reste avec un seul achat, Débloquer toutes les mers. Comment l'encre consommable est prévue dans l'offre de vente, comment le verrou est calculé dans le code, les limites que nous avons fixées pour la restauration et les remboursements, et ce que nous n'avons pas encore testé.
slug: two-free-seas-and-one-unlock
lang: fr
translation_of: en
category: making-of
keywords: Inkisle, achat intégré, non consommable, mers gratuites, restaurer les achats, jeu mobile
image_alt: Deux îles ouvertes, puis une rangée d'îles cadenassées derrière, et une clé posée en travers de la rangée.
---

Inkisle, notre jeu de stratégie de conquête d'îles pour iOS, garde les mers 1 et 2 gratuites et ouvre les mers 3 à 30 (28 mers) avec un seul achat, Débloquer toutes les mers. L'encre consommable (lots de 5 et de 15) figure dans l'offre de vente, mais elle n'est pas publiée et n'a pas été vérifiée sur un appareil. Les six articles de pourboire restent. Les produits de la boutique en sont à l'étape d'enregistrement, mais ils n'ont pas encore été soumis à la révision ni vérifiés sur un appareil ; l'achat n'est donc pas encore confirmé. Le jeu est en développement et n'est pas sorti. Cet article n'indique ni prix ni date.

## Ce qui a changé

La première conception rendait toutes les étapes gratuites, et l'encre qui réduit la difficulté était vendue en petits articles consommables. Le 15 novembre, le responsable a modifié cela. **Les mers 1 et 2 sont gratuites, et Débloquer toutes les mers est un achat unique non consommable.** L'encre consommable (lots de 5 et de 15) figure dans l'offre de vente, mais elle n'est pas publiée et n'a pas été vérifiée sur un appareil. L'encre s'obtient aussi avec les étoiles : une pour 5 étoiles, et 2 pour la victoire contre un boss. L'encre achetée auparavant fonctionne toujours.

## Le verrou est calculé

Le nombre de mers verrouillées n'est pas saisi à la main dans le code. C'est le nombre total de mers moins le nombre de mers gratuites. Aujourd'hui, cela donne 30 − 2 = 28, et quand des mers seront ajoutées, le texte de la feuille d'achat « ouvre N mers » suivra. Le texte de vente que nous avons préparé promet que les nouvelles mers sont incluses.

- Sur la carte, les étapes à partir de la mer 3 portent un cadenas rouge, et un appui sur l'une d'elles ouvre la boutique au lieu de l'étape.
- Acheter ou restaurer les ouvre toutes.
- Après une victoire, si l'étape suivante se trouve dans une mer verrouillée, le jeu revient à la carte.

## L'application doit fonctionner sans produit

Si la boutique n'a pas encore de produit, ou si la récupération du prix échoue, seul le bouton d'achat est désactivé et une mention « bientôt disponible » apparaît. L'application ne plante pas. Le prix est recherché à nouveau à chaque ouverture de la feuille, donc, une fois le produit créé, cela fonctionne sans modifier le code. C'est exactement notre situation actuelle. La création du produit est bloquée côté boutique, et nous n'avons donc jamais exécuté le vrai parcours d'achat.

## Les limites que nous avons fixées volontairement

| Cas | Comportement |
|---|---|
| Un joueur qui a déjà dépassé la mer 2 | Verrouillé. Les enregistrements et les étoiles restent, et un achat ou une restauration les rouvre |
| Un autre appareil | La progression arrive via iCloud, mais le déblocage non. Appuyez sur « Restaurer les achats » à cet endroit |
| Remboursements | Nous ne retirons pas l'accès |
| « Tout ouvrir » dans TestFlight | Supprime le verrou de progression, mais pas le verrou de paiement, afin que le parcours d'achat puisse être testé dans le bac à sable |

Ne pas retirer l'accès après un remboursement est à la fois un choix et une limite. Le paquet `in_app_purchase` de Flutter n'a pas d'état qui signale un remboursement, et à cette échelle, nous avons décidé de ne pas vérifier les reçus sur un serveur. Ce jugement est une estimation [non vérifié].

## Ce que nous n'avons pas vérifié

- Nous n'avons pas acheté ni restauré sur un appareil réel [non vérifié]. Pour l'instant, il y a des tests de widgets (cadenas, boutique, achat, déblocage) et une vérification de la configuration StoreKit.
- Les rendus en 375 px et 320 px ont été couverts par des tests de widgets, et non par un simulateur [non vérifié].
- Android utilise le même chemin de code, mais sans produit enregistré, nous n'avons pas pu tester le paiement là-bas [non vérifié].
- Le texte d'achat dans les 11 langues autres que le coréen est traduit automatiquement [non vérifié].

## Questions fréquentes

### Quelle part d'Inkisle est gratuite ?

Les mers 1 et 2. Les 28 autres mers s'ouvrent ensemble une fois Débloquer toutes les mers acheté. Le jeu n'est pas encore sorti.

### Combien de fois faut-il acheter ?

Une seule fois. C'est un achat non consommable, conçu pour inclure aussi les nouvelles mers.

### Les pourboires influencent-ils le jeu ?

Non. Les six articles de pourboire ne donnent aucun avantage dans le jeu et restent tels quels.
