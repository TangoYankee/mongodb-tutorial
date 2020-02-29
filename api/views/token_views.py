from api import app

from flask import jsonify, request
from flask.views import MethodView

class TokenService(MethodView):
  def get(self, user_id):
    """dev only: test existence of route"""
    return 'token'

  def post(self):
    """Give access and refresh tokens to users"""
    _json = request.json
    pass
  
  def put(self):
    _json = request.json
    pass

  def delete(self, user_id):
    pass
