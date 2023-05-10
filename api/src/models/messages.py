from . import db
from .abc import BaseModel

import datetime

class Message(db.Model, BaseModel):
    """La classe des messages"""

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)
    username = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__ (self, message: str, username:str): 
        self.message = message
        self.username = username

