from lendinglibrary import app
from lendinglibrary.validators.user_schema import UserSchema

from flask import request
from flask.views import MethodView


class UserAPI(MethodView):
    userSchema = UserSchema()
    def get(self, user_id):
        return self.userSchema.get(user_id)

    def post(self):
        _json = request.json
        return self.userSchema.post(_json)

    def delete(self, user_id):
        return self.userSchema.delete(user_id)
