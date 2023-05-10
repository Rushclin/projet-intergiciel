# Modele User 
from flask import request
from connection.connection import Connection

CREATE_USERS_TABLE = ("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, username TEXT);")
INSERT_USER_RETURN_ID = "INSERT INTO users (username) VALUES (%s) RETURNING id;"
GET_USER = """SELECT username FROM users WHERE id = 1"""
# GET_USER = """SELECT id FROM users WHERE username = (%s)"""

class User: 
    def __init__(self):
        self.connection = Connection().init_connection()

    def login(self): 
        self.data = request.get_json()
        self.username = self.data['username'] 
        with self.connection: 
            with self.connection.cursor() as cursor:
                cursor.execute(CREATE_USERS_TABLE)
                cursor.execute(GET_USER, (self.username,))
                
                if cursor.fetchone(): 
                    print(cursor.fetchone())
                    self.id = cursor.fetchone()[0]
                    return {"id": self.id}, 201
               
                cursor.execute(INSERT_USER_RETURN_ID, (self.username,))
                self.id = cursor.fetchone()[0]
                return {"id": self.id}, 201





