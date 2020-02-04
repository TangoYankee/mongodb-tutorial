from os import getenv
from lendinglibrary import app
from flask_pymongo import PyMongo


app.config["MONGO_URI"] = f"mongodb+srv://{getenv('MONGODB_USERNAME')}:{getenv('MONGODB_PASSWORD')}@cluster0-075z2.mongodb.net/lendinglibrarydb?retryWrites=true&w=majority"
mongo = PyMongo(app)
