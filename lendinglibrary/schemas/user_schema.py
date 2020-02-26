"""
Handle the requests to the Mongo Database
"""
from lendinglibrary.database import mongo

from flask import jsonify
from schema import Schema, Optional
from pymongo import MongoClient, ReturnDocument
from bson.objectid import ObjectId
from bson.json_util import dumps
from werkzeug.security import generate_password_hash


class UserSchema:
    """Handle calls for users collection"""
    user_collection = mongo.db.user
    def __init__(self):
        """username and schema are standard to every instance"""
        self.user_schema = Schema({
            "username":         str,
            "email":            str,
            "pwd":              str,
            Optional("books"):  list
            })

    def get(self, user_id):
        """Retrieve values for user from database"""
        if user_id is None:
            users = self.user_collection.find()
            return dumps(users)
        else:
            user = self.user_collection.find_one({'_id' : ObjectId(user_id)})
            return dumps(user)

    def post(self, _json):
        self._json = _json
        try:
            self.is_valid
            self.user_collection.insert_one(self.json_data)
            resp = jsonify('user added')
            resp.status_code = 201
            return resp
        except KeyError as e:
            resp = jsonify(f'missing {e} field')
            resp.status_code = 400
            return resp
         
    def delete(self, user_id):
        if user_id is None:
            resp = jsonify('missing user id')
            resp.status_code = 400
            return resp
        else:
            self.user_collection.delete_one({'_id' : ObjectId(user_id)})
            resp = jsonify('user deleted')
            resp.status_code = 200
            return resp

    @property
    def json_data(self):
        """Translate HTTP Request to JSON
            TODO: Replace with requests"""
        data = {}
        _username, _email, _pwd = self._json['username'], self._json['email'], self._json['pwd']
        if _username and _email and _pwd:
            _hashed_password = generate_password_hash(self._json['pwd'])
            _hashed_password = self._json['pwd']
            data['username'] = self._json['username']
            data['email'] = self._json['email']
            data['pwd'] = _hashed_password
            data['books'] = []
        return data

    @property
    def is_valid(self):
        """Check current data against established schema"""
        return self.user_schema.validate(self.json_data)
