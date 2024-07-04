# Projet 10 SoftDesk

Projet n°10 réalisé dans le cadre de ma formation OpenClassrooms Développeur d'Applications Python.

Il s'agit d'une API réalisée avec Django RestFrameWork pour une société fictive, SoftDesk.

L'application permet de remonter et suivre des problèmes techniques (issue tracking system).

### Fonctionnalités principales

#### Gestion des utilisateurs:

* Inscription et connexion des utilisateurs
* Respect de la confidentialité des utilisateurs
* Conformité au RGPD avec vérification de l'âge

#### Gestion des projets:

* Création de projets et définition des auteurs et contributeurs
* Enregistrement des détails du projet (nom, description, type)
* Accès limité aux contributeurs du projet

#### Création de problèmes:

* Création de problèmes par les contributeurs pour un projet spécifique
* Assignation des problèmes aux contributeurs
* Définition de la priorité et des balises pour chaque problème
* Suivi de l'avancement avec des statuts (À faire, En cours, Terminé)

#### Création de commentaires:

* Ajout de commentaires par les contributeurs pour faciliter la communication
* Association des commentaires aux problèmes spécifiques
* Identification unique de chaque commentaire
* Informations complémentaires
* Horodatage de toutes les ressources

#### Possibilité pour les auteurs de modifier ou supprimer leurs propres ressources

* Pagination pour optimiser le chargement des listes de ressources
* Tests des points de terminaison de l'API pour garantir un bon fonctionnement

## Technologies utilisées
* [Django](https://www.djangoproject.com/)
* [DRF](https://wwww.django-rest-framework.org/)
* [POSTMAN](https://www.postman.com/)

## Installation
* Prérequis : Python 3.x installé sur votre système
* Un environnement virtuel Python activé.

* Lancez ensuite la console, placez vous dans le dossier de votre choix puis clonez ce repository.
* Vous pouvez vous procurer python [ici](https://www.python.org").
* créez un nouvel environnement virtuel sous windows :
    ```bash
        python - m venv /path/to/new/virtualenvironment
     ```
* Ensuite, activez-le (sous Windows) :
    ```bash
        /path/to/new/virtualenvironment\scripts\activate.bat
    ```

* #### Dépendances :
 * Installez et activez poetry pour vous assurer de la maintenance des dépendances:

    ```bash
        pip install poetry
        poetry install
    ```
* Effectuez les migrations
* 
   ```bash
       python manage.py makemigrations
       python manage.py migrate
   ```

* #### Démarrez le serveur :
    ```bash
        python manage.py runserver
    ```
* #### Conception API

* #### "api/users": "http://127.0.0.1:8000/api/users/",
* #### "api/projects": "http://127.0.0.1:8000/api/projects/",
* #### "api/issue": "http://127.0.0.1:8000/api/projects/{pk}/issues/",
* #### "api/comments": "http://127.0.0.1:8000/api/projects/{pk}/issues/",
* #### "api/contributor": "http://127.0.0.1:8000/api/projects/{pk}/contributors/",
* #### "signup": "http://127.0.0.1:8000/signup/"
