from sqlalchemy.exc import IntegrityError
from exception import ResourceExists
from models import Message

class  MessageRepository: 
    """Classe qui doit gerer les fonctions de messages"""

    @staticmethod
    def create(message: str, username: str) -> dict: 
        """Create a new message"""
        result: dict = {}

        try: 
            message = Message(message=message, username=username)
            message.save()
            result = {
                'username': message.username, 
                'message': message.message, 
                'date_created': str(message.date_created)
            }
        except IntegrityError: 
            Message.roolback()

        return result
    
    @staticmethod
    def get() -> dict: 
        """Recuperation de tous les messages"""
        result = []
        messages = Message.query.all()
        for message in messages: 
            result.append({
                "username": message.username, 
                "message": message.message, 
                "date_created": str(message.date_created), 
            })
        Message.commit()
        return result
