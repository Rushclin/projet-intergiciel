from flask_restful import Api
from flask_migrate import Migrate
from resources import HealthCheck, User, UserList, MessagePost, Message

from models import User as UserModel, Message as MessageModel, db
from app import create_app

app = create_app()
migrate = Migrate(app, db)

# API
api = Api(app)
api.add_resource(HealthCheck, '/healthcheck') # Verification que le serveur fonctionne (GET)
api.add_resource(UserList, '/api/users') # Pour faire un post (Creer un utilisateur) (POST)
api.add_resource(User, '/api/user/<username>') # pour la recuparation (GET avec un parametre)
api.add_resource(Message, '/api/messages') # pour reuperertous les messages (GET)
api.add_resource(MessagePost, '/api/message') # Pour poster un message (POST)
# CLI for migrations
@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=UserModel, Message=MessageModel)
