from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .abc import BaseModel
from .user import User
from .messages import Message

__all__ = ['BaseModel','User', 'Message']