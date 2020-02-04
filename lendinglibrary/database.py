from os import getenv
from lendinglibrary import app
from flask_pymongo import PyMongo


app.config["MONGO_URI"] = f"mongodb+srv://lendinglibrary:{getenv['MONGODB_PASSWORD']}@cluster0-075z2.mongodb.net/test?retryWrites=true&w=majority"
mongo = PyMongo(app)
