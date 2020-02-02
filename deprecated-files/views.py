from app import UserAPI
from settings import app

user_view = UserAPI.as_view('user_api')
app.add_url_rule('/users/', defaults={'user_id':None},view_func=user_view, methods=['GET',])
