# Gestion de Drive

## À propos du projet


L'application reproduit le fonctionnement simplifié d'un service de Drive où les clients peuvent passer des commandes parmi différents produits disponibles.

---

## Fonctionnalités

L'application permet de gérer plusieurs types de données :

### Les catégories

Les catégories servent à classer les produits selon leur nature (boissons, produits laitiers, épicerie, etc.).

Pour chaque catégorie, il est possible de :

- ajouter une catégorie ;
- consulter les catégories existantes ;
- modifier une catégorie ;
- supprimer une catégorie.

### Les produits

Chaque produit possède :

- un nom ;
- une date de péremption ;
- une photo ;
- une marque ;
- un prix ;
- une catégorie.

Les fonctionnalités disponibles sont :

- ajout d'un produit ;
- affichage de la liste des produits ;
- modification des informations d'un produit ;
- suppression d'un produit ;
- importation de produits via un fichier CSV.

### Les clients

Chaque client est enregistré avec :

- son numéro client ;
- son nom ;
- son prénom ;
- sa date d'inscription ;
- son adresse.

Il est possible de créer, consulter, modifier et supprimer un client.

### Les commandes

Les clients peuvent passer des commandes composées de plusieurs produits.

Pour chaque commande, l'application permet :

- de sélectionner un client ;
- d'ajouter plusieurs produits ;
- de définir une quantité pour chaque produit ;
- de consulter le détail de la commande ;
- de modifier ou supprimer une commande.

---

## Base de données

La base de données a été préparée en amont avec plusieurs données de démonstration afin de faciliter les tests de l'application.

Elle contient :

- des catégories ;
- des produits ;
- des clients.

Les commandes sont créées directement depuis l'interface.

---


## Fiche de commande

Une fois une commande créée, l'application génère automatiquement une fiche récapitulative contenant :

- les informations du client ;
- la date de la commande ;
- les produits commandés ;
- les quantités ;
- le prix de chaque produit ;
- le montant total de la commande.

Cette fonctionnalité permet d'avoir un aperçu clair de la commande avant sa validation.

---

## Technologies utilisées

Pour réaliser ce projet, plusieurs technologies ont été utilisées :

- HTML
- CSS
- Django
- MySQL

---

## Ce que nous avons appris

Grâce à ce projet, j'ai pu approfondir plusieurs notions importantes :

- la conception d'une base de données relationnelle ;
- la gestion des relations entre différentes tables ;
- la réalisation d'opérations CRUD ;
- le traitement des formulaires ;
- l'importation de données depuis un fichier ;
- la génération d'un récapitulatif de commande ;
- le développement d'une application web complète connectée à une base de données.

---

## Auteur
Koch Vincent, Prevot Justin, Dfil Ayoub
