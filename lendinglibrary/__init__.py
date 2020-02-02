"""Initialize app"""
from flask import Flask


app = Flask(__name__)
from lendinglibrary import urls
