from api import app

from flask import jsonify, request
from flask.views import MethodView
from api.jwt_config import jwt
from flask_jwt_extended import (
  create_access_token, create_refresh_token,
  set_access_cookies, set_refresh_cookies,
  jwt_refresh_token_required, unset_jwt_cookies
)

class TokenService(MethodView):
  def post(self):
    """Give access and refresh tokens to users"""
    _json = request.json
    user_id = _json.get('user_id', None)
    pwd = _json.get('pwd', None)
    if user_id != 'test' or pwd != 'test':
      return jsonify({'token created' : False}), 401
    access_token = create_access_token(identity=user_id)
    refresh_token = create_refresh_token(identity=user_id)
    resp = jsonify({'token create': True})
    set_access_cookies(resp, access_token)
    set_refresh_cookies(resp, refresh_token)
    return resp, 200

  @jwt_refresh_token_required
  def put(self):
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)
    resp = jsonify({'token refresh': True})
    set_access_cookies(resp, access_token)
    return resp, 200

  def delete(self):
    resp = jsonify({'token remove': True})
    unset_jwt_cookies(resp)
    return resp, 200
