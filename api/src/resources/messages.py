from flask import request, jsonify
from flask_restful import Resource

from repositories import MessageRepository

class Message(Resource): 
    """Classe qui doit faire les appel APIs"""

    def get(self): 
        messages = MessageRepository.get()
        return messages, 200
    
class MessagePost(Resource):
    def post(self): 
        """Creation d'un message"""

        request_json = request.get_json(silent=True)
        username: str = request_json['username']
        message: str = request_json['message']
        try:
            messages = MessageRepository.create(
                username, 
                message
            )
            return messages, 200
        except Exception as e: 
            response = jsonify(e.to_dict())
            response.status_code = e.status_code 
            return response
