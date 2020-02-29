from os import getenv
from api import app
from flask_pymongo import PyMongo

# app.config["MONGO_DBNAME"] = 'lendingLibraryDB'
# app.config["MONGO_URI"] = f"mongodb+srv://{getenv('MONGODB_USERNAME')}:{getenv('MONGODB_PASSWORD')}@cluster0-075z2.mongodb.net/lendinglibrarydb?retryWrites=true&w=majority"
# app.config["MONGO_URI"] = "mongodb://localhost:27017/lendingLibraryDB"
app.config["MONGO_URI"] = getenv('MONGO_URI')
mongo = PyMongo(app)
