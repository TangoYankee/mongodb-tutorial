from lendinglibrary import app
from flask_pymongo import PyMongo

app.config["MONGO_URI"] = "mongodb://localhost:27017/lendingLibraryDB"
mongo = PyMongo(app)
