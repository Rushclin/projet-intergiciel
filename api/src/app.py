from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import get_config

db = SQLAlchemy()

def create_app(env=None): 
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(get_config(env))
    db.init_app(app)
    return app