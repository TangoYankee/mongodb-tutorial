from settings import app, mongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import request, jsonify
from flask.views import MethodView
from werkzeug import generate_password_hash


class UserAPI(MethodView):
    def get(self, user_id):
        if user_id is None:
            users = mongo.db.user.find()
            return dumps(users)
        else:
            user = mongo.db.user.find_one({'_id' : ObjectId(user_id)})
            return dumps(user)

    def post(self):
        _json = request.json
        _username = _json['username']
        _email = _json['email']
        _password = _json['pwd']
        if _username and _email and _password:
            _hashed_password = generate_password_hash(_password)
            mongo.db.user.insert({
                'username': _username,
                'email': _email,
                'pwd': _hashed_password
            })
            resp = jsonify('user added')
            resp.status_code = 201
            return resp
        else:
            resp = jsonify('missing required field')
            resp.status_code = 400
            return resp

    def delete(self, user_id):
        if user_id is None:
            resp = jsonify('missing user id')
            resp.status_code = 400
            return resp
        else:
            mongo.db.user.delete_one({'_id' : ObjectId(user_id)})
            resp = jsonify('user deleted')
            resp.status_code = 200
            return resp
    

def register_api(view, endpoint, url, pk='id', pk_type='string'):
    view_func = view.as_view(endpoint)
    app.add_url_rule(url, defaults={pk:None},view_func=view_func, methods=['GET',])
    app.add_url_rule(url, view_func=view_func, methods=['POST',])
    app.add_url_rule('%s<%s:%s>'% (url, pk_type, pk), view_func=view_func, methods=['GET' ,'PUT' ,'DELETE' ])
    
register_api(UserAPI,'user_api','/users/', pk='user_id')


if __name__== "__main__":
    app.run()
