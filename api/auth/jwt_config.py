from os import getenv
from flask_jwt_extended import JWTManager
from api import app

app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_ACCESS_COOKIE_PATH'] = '/api/v1/'
app.config['JWT_REFRESH_COOKIE_PATH'] = '/token/refresh'

app.config['JWT_COOKIE_CSRF_PROTECT'] = False

app.config['JWT_SECRET_KEY'] = getenv('JWT_SECRET_KEY')

jwt = JWTManager(app)
