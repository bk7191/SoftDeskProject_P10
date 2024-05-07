# Projet 10 SoftDesk

Projet réalisé dans le cadre de ma formation OpenClassrooms Développeur d'Applications Python.

Il s'agit d'une API réalisée avec Django RestFrameWork pour une société fictive, SoftDesk.
L'application permet de remonter et suivre des problèmes techniques (issue tracking system).

## Technologies utilisées
* [Django](https://www.djangoproject.com/)
* [DRF](www.django-rest-framework.org/)


## Installation
* Prérequis : Python 3.x installé sur votre système
* Un environnement virtuel Python activé.

* Lancez ensuite la console, placez vous dans le dossier de votre choix puis clonez ce repository. 
* Vous pouvez vous procurer python [here](https://www.python.org").
* créez un nouvel environnement virtuel:
    ```bash
        pip install virtualenv
    ```
* Ensuite, activez-le (sous Windows) :
    ```bash
        env\scripts\activate.bat
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

