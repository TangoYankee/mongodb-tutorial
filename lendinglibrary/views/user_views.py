from lendinglibrary import app
from lendinglibrary.schemas.user_schema import UserSchema

from flask import request
from flask.views import MethodView


class UserAPI(MethodView):
    user_schema = UserSchema()
    def get(self, user_id):
        return self.user_schema.get(user_id)

    def post(self):
        _json = request.json
        return self.user_schema.post(_json)

    def delete(self, user_id):
        return self.user_schema.delete(user_id)
