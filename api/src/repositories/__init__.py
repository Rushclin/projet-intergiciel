from flask_sqlalchemy import SQLAlchemy
from .user import UserRepository
from .messages import MessageRepository


db = SQLAlchemy()
__all__ = ['UserRepository', 'MessageRepository']
