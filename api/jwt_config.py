from os import getenv
from api import app
from flask_jwt_extended import JWTManager

app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_ACCESS_COOKIE_PATH'] = '/api/v1/'
app.config['JWT_REFRESH_COOKIE_PATH'] = '/token/'


app.config['JWT_COOKIE_SECURE'] = False
app.config['JWT_COOKIE_CSRF_PROTECT'] = True
app.config['JWT_SECRET_KEY'] = getenv('JWT_SECRET_KEY')

jwt = JWTManager(app)
