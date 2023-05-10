# BLUE CHAT (API)

Application interactive de Chat.

## Installation

Pour deployer notre application (API) chez vous, vous pouvez suivre la procedure.

1. Cloner le projet
   Pour cloner le projet suivre la procedure

   ```
       git clone https://github.com/
   ```

2. Créer l'environment virtuel
   Pour créer l'environment virtuel, utiliser la commande suivante:

   ```
       cd api
       python -m venv venv
       source .venv/bin/activate   # Marche uniquement sur Linux
       ./venv/Scripts/activate

   ```

3. Installation des dependences
   Nous utilisons python. Donc pour installer les dependences, suivre la procedure
   ```
       pip install -r requirements.txt
   ```
4. Creation du fichier .env
   Creer le fichier .env à la racine (donc dans le dossier api), mettre la configuration suivante

   ```
       POSTGRES_USER = 'postgres'
       POSTGRES_PASSWORD = 'root' # Les données vont changer selon l'utilisateur
       POSTGRES_DB = 'chat' # Idem ici
       POSTGRES_URL = 'localhost:5432' # Idem ici
       FLASK_APP="src/main.py"
   ```

5. Executer les migrations
   Pour executer les migrations, suivre les etatpes suivantes
   ```
       flask db init
       flask db migrate
       flask db upgrade
   ```
6. Demarrer le projet
   ```
       flask run
   ```

## Voir que le projet est bien demarré.

    Visiter le lien suivant

    http://localhost:5000/healthcheck

## License

    Ce projet n'est sous aucune licence.

## Credits

    - flake8
    - Flask
    - Flask-Migrate
    - Flask-RESTful
    - Flask-SQLAlchemy
    - gunicorn
    - mypy
    - psycopg2
    - pytest-flask
    - requests
    - shortuuid
    - SQLAlchemy
