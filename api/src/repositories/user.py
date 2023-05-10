from sqlalchemy.exc import IntegrityError
from exception import ResourceExists
from models import User

class UserRepository: 
    """Classe qui doit gerer les appels fonctions concernant l'objet User """

    @staticmethod
    def create(username: str, avatar_url: str) -> dict: 
        """Creation d'un nouvel utilisateur"""
        result : dict = {}

        try: 
            user = User(username=username, avatar_url=avatar_url)
            user.save()
            result = {
                'username': user.username,
                'avatar_url': user.avatar_url,
                'date_created': str(user.date_created)
            }
        except IntegrityError: 
            User.roolback()
            raise ResourceExists("L'utilisateur existe déjà")
        
        return result
    
    @staticmethod 
    def get(username: str) -> dict: 
        """Recuperation d'un utilisateur avec son username"""
        user: dict = {}
        user = User.query.filter_by(username=username).first_or_404()
        user = {
            "username": user.username,
            "date_created": str(user.date_created)
        }
        return user