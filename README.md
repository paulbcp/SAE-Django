# SAE-Django

# Gestion de Drive – Application Web

## Présentation

Cette application web permet la gestion complète d'un Drive. Elle offre aux utilisateurs la possibilité de gérer les produits, les catégories, les clients et les commandes, tout en assurant le suivi des achats effectués par les clients.

L'objectif du projet est de mettre en œuvre une interface de gestion reposant sur un système CRUD (Create, Read, Update, Delete) pour l'ensemble des données du Drive.

---

## Fonctionnalités

### Gestion des catégories de produits

Chaque catégorie contient les informations suivantes :

- Identifiant
- Nom
- Descriptif

Fonctionnalités disponibles :

- Ajouter une catégorie
- Consulter la liste des catégories
- Modifier une catégorie
- Supprimer une catégorie

---

### Gestion des produits

Chaque produit contient les informations suivantes :

- Identifiant
- Nom
- Date de péremption
- Photo
- Marque
- Prix
- Catégorie associée

Fonctionnalités disponibles :

- Ajouter un produit
- Consulter les produits
- Modifier un produit
- Supprimer un produit
- Importer plusieurs produits depuis un fichier

---

### Gestion des clients

Chaque client contient les informations suivantes :

- Numéro de client
- Nom
- Prénom
- Date d'inscription
- Adresse

Fonctionnalités disponibles :

- Ajouter un client
- Consulter les clients
- Modifier un client
- Supprimer un client

---

### Gestion des commandes

Chaque commande contient :

- Numéro de commande
- Client associé
- Date de commande

Une commande est composée d'une liste de produits avec leur quantité.

Fonctionnalités disponibles :

- Créer une commande
- Ajouter des produits à une commande
- Modifier une commande
- Supprimer une commande
- Consulter l'historique des commandes

---

## Modèle de données

### Catégorie

| Champ | Type |
|---------|---------|
| id | Integer |
| nom | String |
| descriptif | Text |

### Produit

| Champ | Type |
|---------|---------|
| id | Integer |
| nom | String |
| date_peremption | Date |
| photo | String |
| marque | String |
| prix | Decimal |
| categorie_id | Integer |

### Client

| Champ | Type |
|---------|---------|
| numero_client | Integer |
| nom | String |
| prenom | String |
| date_inscription | Date |
| adresse | String |

### Commande

| Champ | Type |
|---------|---------|
| numero_commande | Integer |
| client_id | Integer |
| date_commande | Date |

### LigneCommande

| Champ | Type |
|---------|---------|
| commande_id | Integer |
| produit_id | Integer |
| quantite | Integer |

---

## Initialisation de la base de données

Avant le lancement de l'application, la base de données doit être préremplie avec :

- Des catégories de produits
- Des produits
- Des clients

Ces données permettront de tester rapidement les fonctionnalités du site.

---

## Import de produits par fichier

L'application permet l'ajout de produits via un fichier d'import.

### Format attendu (CSV)

```csv
nom;date_peremption;photo;marque;prix;categorie
Lait Demi-Ecreme;2025-12-31;lait.jpg;Candia;1.29;Produits laitiers
Pates;2027-01-15;pates.jpg;Barilla;2.10;Epicerie
Jus d'Orange;2025-08-01;jus.jpg;Tropicana;3.50;Boissons
