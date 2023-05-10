# Class qui doit etablir la connexion 
import os 
import psycopg2
from dotenv import load_dotenv

load_dotenv()

URL = os.environ.get("DATABASE_URL")
CONNECTION = psycopg2.connect(URL)

class Connection: 
    """ Classe qui doit etablir la connexion avec la BD ElephantSQL """
    def __init__(self):
        pass 

    def init_connection(self): 
        return CONNECTION
