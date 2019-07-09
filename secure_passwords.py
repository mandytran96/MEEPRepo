from cryptography.fernet import Fernet
import pymongo
import os
import urllib.parse
from pymongo import MongoClient
CREDS = "<PASSWORD>"
client = pymongo.MongoClient("mongodb+srv://root:" +urllib.parse.quote(CREDS)+ "@cluster0-i0lbe.mongodb.net/test?retryWrites=true&w=majority")
db = client.users

class VaultKeeper():
    password = None
    key = None
    token = None
    def __init__(self,passwordIn):
        self.password = passwordIn

    def addUser(self,username):

        self.key = Fernet.generate_key()
        fern = Fernet(self.key)
        self.token = fern.encrypt(bytes(self.password,'utf-8'))

        user = {
            "username": username,
            "password": self.token,
            "key": self.key
        }
        db.users.insert_one(user)

    def findUser(self,username):
        for i in db.users.find({}):
            if username in i.get('username'):
                return True
        return False
class Grab():
    def findUser(self,username):
        for i in db.users.find({}):
            if username in i.get('username'):
                return True
        return False

    def decrypt(self,username,password):
        user = db.users.find({"username": username})
        for i in db.users.find({}):
            if username in i.get('username'):
                key = i['key']
                f = Fernet(key)
                passw = f.decrypt(i['password'])
                if password == passw:
                    return True
        return False





