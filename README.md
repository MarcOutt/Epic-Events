[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
# Développez une architecture back-end sécurisée en utilisant Django ORM
-------------------------------------------------------------------


## TABLE DES MATIERES
---------------------

* Introduction
* Pré-requis
* Installation
* Démarrage
* Documentation API
* Rapport de test
* Rapport Flake8


## INTRODUCTION
----------------

Ce projet consite à créer une API sécurisée RESTFUL pour un CRM.
Le système CRM permet la gestion des processus métier pour tous les acteurs concernés, afin que chacun dispose des informations dont il a besoin.


Fonctionnalités de haut niveau requises :
* Stocker les informations sur nos clients.
* Permettre la conversion des clients potentiels en clients existants.
* Pouvoir stocker les informations sur les nouveaux contrats signés par les clients existants pour un événement.
* Créer de nouveaux événements (une fois qu'un client signe un contrat).
* Actualiser les informations sur l'événement lorsque cela est nécessaire, jusqu'au terme de ce dernier.
* Tous les membres de l'équipe de management doivent : 
   * Créer, mettre à jour et supprimer des utilisateurs dans le système CRM, en restreignant leur accès à certaines données.
   * Afficher et modifier toutes les données dans le système CRM
* Tous les membres de l'équipe de vente doivent avoir :
    * Un accès en lecture seule à tous les clients, contrats ou événements.
    * Un droit de modification/d'accès pour tous les clients dont ils sont responsables, ainsi que pour leurs contrats et événements.
* Tous les membres de l'équipe de support doivent avoir :
    * Un accès en lecture seule à tous les clients, contrats ou événements.
    * Un droit de modification/d'accès pour tous les événements dont ils sont responsables.


## PRÉ-REQUIS
-------------

* Installer Python 3 : [Téléchargement Python 3](https://www.python.org/downloads/)
* Installer git : [Téléchargement Git](https://git-scm.com/book/fr/v2/D%C3%A9marrage-rapide-Installation-de-Git)
* Installer POSTGRESQL : [Téléchargement POSTGRESQL](https://www.postgresql.org/download/)


## INSTALLATION
------------------

### 1. Télécharger le projet sur votre répertoire local : 
```
git clone https://github.com/MarcOutt/OC_p12.git
```
### 2. Mettre en place un environnement virtuel :
* Créer l'environnement virtuel: `python -m venv venv`
* Activer l'environnement virtuel :
    * Windows : `venv\Scripts\activate.bat`
    * Unix/MacOS : `source venv/bin/activate`
    
### 3. Installer les dépendances du projet
```
pip install -r requirements.txt
```


## UTILISATION
--------------

* Naviguer dans le dossier src et entrez la commande suivante dans le terminal pour lancer le serveur :

```bash
python manage.py runserver
```

Afin de tester les différentes fonctionalités du site, 3 comptes utilisateurs ont été créés : 
* Identifiant: r.lapierre@ee.com ; mot de passe: test_password ; rôle: management  
* Identifiant: p.delacour@ee.com ; mot de passe: test_password ; rôle: sale  
* Identifiant: p.laroche@ee.com ; mot de passe: test_password ; rôle: support  


## POINT DE TERMINAISON D'API  MÉTHODE HTTP 
-------------------------------------------

1. Création d'utilisateur POST http://127.0.0.1:8000//users/
2. Récupérer la liste de tous les utilisateurs GET http://127.0.0.1:8000//users/
3. Récupérer un utilisateur GET http://127.0.0.1:8000//users/{user_id}/
4. Mettre à jour un utilisateur PATCH http://127.0.0.1:8000//users/{user_id}/
5. Supprimer un utilisateur DELETE http://127.0.0.1:8000//users/{user_id}/
6. Connexion de l'utilisateur POST http://127.0.0.1:8000/

7. Création d'un client POST http://127.0.0.1:8000//customers/
8. Récupérer la liste de tous les clients GET http://127.0.0.1:8000//customers/
9. Récupérer un client GET http://127.0.0.1:8000//customers/{customers_id}/
10. Mettre à jour un client PUT http://127.0.0.1:8000//customers//{customers_id}/
11. Supprimer un client DELETE http://127.0.0.1:8000//users/{customers_id}/

12. Création d'un contrat lié à un client POST http://127.0.0.1:8000//customers/{customers_id}/contracts/
13. Récupérer la liste de tous les contrats lié à un client GET http://127.0.0.1:8000//customers/{customers_id}/contracts/
14. Récupérer un contrat GET http://127.0.0.1:8000//customers/{customers_id}/contracts/{contract_id}/
15. Mettre à jour un contrat PUT http://127.0.0.1:8000//customers/{customers_id}/contracts/{contract_id}/
16. Supprimer un contrat DELETE http://127.0.0.1:8000//customers/{customers_id}/contracts/{contract_id}/

17. Création d'un event lié à un contrat POST http://127.0.0.1:8000//customers/{customers_id}/contracts/{contract_id}/events/
18. Récupérer la liste de tous les events lié à un contrat GET http://127.0.0.1:8000//customers/{customers_id}/contracts/{contract_id}/events/
19. Récupérer un event GET http://127.0.0.1:8000//customers/{customers_id}/contracts/{contract_id}/events/{event_id}/
20. Mettre à jour un event PUT http://127.0.0.1:8000//customers/{customers_id}/contracts/{contract_id}/events/{event_id}/
21. Supprimer un event DELETE http://127.0.0.1:8000//customers/{customers_id}/contracts/{contract_id}/events/{event_id}/


## DOCUMENTATION API
---------------------

Vous trouverez ci-dessous le lien vers la documentation de l'API:
https://documenter.getpostman.com/view/23302485/2s93XwyPHZ


## RAPPORT DE TEST
-------------------

Les tests concernant les fonctionnalités de l'application ont été réalisé avec pytest, la couverture de test est de 93 %.
Le rapport des tests peut être trouvé dans le fichier coverage.


## RAPPORT FLAKE8
-------------------

* Ouvrir l'invite de commande ( se reporter à la rubrique installation)
* Lancer votre environnement virtuel ( se reporter à la rubrique installation)
* Rentrer le code suivant:

```bash
flake8 --exclude=.env/,unit_test,migrations,htmlcov,create_user.py  --max-line-length=119 --format=html --htmldir=flake8-rapport
``` 

* Aller dans le dossier flake8-rapport
* Ouvrir le fichier index
