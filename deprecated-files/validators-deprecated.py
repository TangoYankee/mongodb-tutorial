"""
Handle the requests to the Mongo Database
"""
from schema import Schema, Optional, Or
from pymongo import MongoClient, ReturnDocument
from bson import ObjectId

CLIENT = MongoClient('localhost', 27017)
DB = CLIENT.lending_library

class User:
    """Handle calls for users collection"""
    def __init__(self, username):
        """username and schema are standard to every instance"""
        self.username = username
        self.user_schema = Schema({
            "username":         str,
            "firstname":        str,
            "lastname":         str,
            Optional("books"):  list
            })

    def get(self):
        """Retrieve values for user from database"""
        try:
            user = DB.users.find_one({'username': self.username})
            statement = f'{user}'
        except:
            statement = "error"
        return statement

    def post(self, firstname, lastname):
        """Create validated and json formatted user document"""
        self.firstname = firstname
        self.lastname = lastname
        try:
            self.valid
            DB.users.insert_one(self.json_data)
            statement = f'{self.json_data}'
        except:
            statement = 'invalid'
        return statement

    def delete(self):
        """Remove user document from collection"""
        try:
            DB.users.remove({"username": self.username})
            statement = f'{self.username} removed'
        except:
            statement = 'error'
        return statement

    @property
    def json_data(self):
        """Translate HTTP Request to JSON
            TODO: Replace with requests"""
        return {
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "books": []
            }

    @property
    def valid(self):
        """Check current data against established schema"""
        return self.user_schema.validate(self.json_data)

class Book:
    """Handle collection for books"""
    def __init__(self, title):
        """Title and Schema are standard to all requests"""
        self.title = title
        self.book_schema = Schema({
            "title": str,
            "year": str,
            Optional("borrower"): Or(str, None)
            })

    def get(self):
        """Retrieve values for book from database"""
        try:
            book = DB.books.find_one({'title': self.title})
            statement = f'{book}'
        except:
            statement = "error"
        return statement

    def post(self, year, borrower):
        """Create book based on preset schema"""
        self.year = year
        self.borrower = borrower
        self.json_data
        try:
            self.valid
            DB.books.insert_one(self.json_data)
            statement = f'{self.json_data}'
        except:
            statement = 'invalid data'
        return statement

    def delete(self):
        """Remove book, only if it is not checked out"""
        try:
            book = DB.books.find_one({"title": self.title}, {'borrower': 1})
            borrower = book['borrower']
            if not borrower:
                try:
                    DB.books.remove({"title": self.title})
                    statement = f'{self.title} removed'
                except:
                    statement = 'removal error'
            else:
                statement = f'this book is checked out by {borrower}'
        except:
            statement = 'title error'
        return statement

    @property
    def json_data(self):
        """Convert HTTP request into JSON format"""
        return  {
            "title": self.title,
            "year": self.year,
            "borrower": self.borrower
            }

    @property
    def valid(self):
        """Check against preset Schema"""
        return self.book_schema.validate(self.json_data)

class Library:
    """Manage functions that act on all documents in a collection"""
    def get(self, collection):
        """get all documents from a collection"""
        if collection == 'books':
            collection = DB.books
        elif collection == 'users':
            collection = DB.users
        else:
            return 'please provide valid collection'
        try:
            items = collection.find()
            statement = []
            for item in items:
                statement.append({'id': ObjectId(item['_id']), 'username': item['username'], 'firstname': item['firstname']})
        except:
            statement = 'an unknown error occured'
        return statement

    def reset(self, collection):
        """Remove all documents from a collection"""
        if collection == 'books':
            collection = DB.books
        elif collection == 'users':
            collection = DB.users
        else:
            return 'please provide valid collection'
        try:
            collection.remove()
            statement = f'{collection} reset'
        except:
            statement = 'error'
        return statement

    def checkin(self, title, username):
        """Return a book to the library"""
        try:
            book = DB.books.find_one_and_update({
                '$and':[{'title': title}, {'borrower': username}]}, {
                    '$set':{"borrower": None}}, return_document=ReturnDocument.AFTER)
            book_id = book['_id']
            DB.users.update_one(
                {"username": username},
                {'$pull': {"books": book_id}})
            statement = f'{book}'
        except:
            statement = 'unable'
        return statement

    def checkout(self, title, username):
        """Assign a book to a borrower"""
        book = DB.books.find_one_and_update({
            '$and':[{'title' : title}, {'borrower' : None}]}, {
                '$set' : {"borrower" : username}}, return_document=ReturnDocument.AFTER)
        book_id = book['_id']
        DB.users.update_one({
            "username" : username}, {
                "$push":{"books": book_id}})
        statement = f'{book}'
        return statement
