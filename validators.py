from schema import Schema, Optional
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.mongodb_tutorial

class User:
    def __init__(self, username):
        self.username = username
        self.collection = db.users
        self.user_schema = Schema({
                    "username":         str,
                    "firstname":        str,
                    "lastname":         str,
                    Optional("books"):  list
                })

    def get(self):
        try:
            user = self.collection.find_one({'username': self.username})
            statement = f'{user}'
        except:
            statement = "error"
        return statement

    def post(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.json_data
        try:
            self.valid
            self.collection.insert_one(self.json_data)
            statement = f'{self.json_data}'
        except:
            statement = 'invalid'
        return statement

    def delete(self):
        try:
            self.collection.remove({"username": self.username})
            statement = f'{self.username} removed'
        except:
            statement = 'error'
        return statement

    @property
    def json_data(self):
        return  {
                    "username": self.username,
                    "firstname": self.firstname,
                    "lastname": self.lastname,
                    "books": []
                }

    @property
    def valid(self):
        return self.user_schema.validate(self.json_data)

class AllUsers:
    def __init__(self):
        self.collection = db.users

    @property
    def get(self):
        try:
            users = self.collection.find()
            statement = ''
            for user in users:
                statement = statement + (f'{user}<br>')
        except:
            statement = 'an unknown error occured'
        return statement