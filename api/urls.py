from api import app
from api.users.views import UserAPI
from api.tokens.views import TokenService
from flask import request


def register_api(view, endpoint, url, pk='id', pk_type='string'):
    view_func = view.as_view(endpoint)
    app.add_url_rule(url, defaults={pk:None},view_func=view_func, methods=['GET',])
    app.add_url_rule(url, view_func=view_func, methods=['POST',])
    app.add_url_rule('%s<%s:%s>'% (url, pk_type, pk), view_func=view_func, methods=['GET' ,'PUT' ,'DELETE' ])
    
register_api(UserAPI,'user_api','/api/v1/users/', pk='user_id')
register_api(TokenService, 'token_service', '/token/', pk='user_id')
