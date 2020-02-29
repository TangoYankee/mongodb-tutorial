from api import app
from api.views.user_views import UserAPI
from api.views.token_views import TokenService
from flask import request


def register_api(view, endpoint, url, pk='id', pk_type='string'):
    view_func = view.as_view(endpoint)
    app.add_url_rule(url, defaults={pk:None},view_func=view_func, methods=['GET',])
    app.add_url_rule(url, view_func=view_func, methods=['POST',])
    app.add_url_rule('%s<%s:%s>'% (url, pk_type, pk), view_func=view_func, methods=['GET' ,'PUT' ,'DELETE' ])
    
register_api(UserAPI,'user_api','/api/v1/users/', pk='user_id')
register_api(TokenService, 'token_service', '/token/', pk='user_id')


# # poor scheme for urls as it puts verbs into the urls
# app.add_url_rule('/token/auth/', 'token_auth', login)
# app.add_url_rule('/token/refresh/', 'token_refresh', refresh)
# app.add_url_rule('/token/remove/', 'token_remove', logout)

def index():
    return 'Hello World!'
index.provide_automatic_options = False
index.methods = ['GET']

app.add_url_rule('/', 'index', index)
