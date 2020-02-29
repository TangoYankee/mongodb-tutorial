from api import app

from flask import jsonify, request
from auth.jwt_config import jwt
from flask_jwt_extended import create_access_token, create_refresh_token

# @app.route('/token/auth/', methods=['GET', 'POST'])
def login():
  return 'login'
  # _json = request.json
  # username = _json.get('username', None)
  # password = _json.get('password', None)
  # if username != 'test' or password != 'test':
  #   return jsonify({'login': False}), 401
  # access_token = create_access_token(identity=username)
  # refresh_token = create_refresh_token(identity=username)

def refresh():
  return 'refresh'

def logout():
  return 'logout'
