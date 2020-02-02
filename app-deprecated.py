"""
Contains all views for application
"""

from flask import Flask, jsonify
from validators import User, Book, Library

app = Flask(__name__)
app.debug = True

LIBRARY = Library()

@app.route("/api/v1/<collection>/", methods=['GET'])
def api_get_collection(collection=None):
    """Get all items in a collection"""
    statement = LIBRARY.get(collection)
    # return statement
    return jsonify({collection: statement})

@app.route("/")
def index():
    """default routing provides reference to all routes"""
    return 'Please follow links to make use of Mongo Database: <br>' \
        '1. /users/ - get all users <br>' \
        '2. /users/username/ - get particular user <br>' \

# URIs should only be nouns. Discard 'GET' from uri!!!!!
@app.route("/users/get/")
@app.route("/users/get/<username>")
def get_user(username=None):
    """get a specific user by username"""
    if username:
        user = User(username)
        statement = user.get()
    else:
        statement = 'please provide a username'
    return statement

@app.route("/users/post/<username>/<firstname>/<lastname>")
def post_user(username=None, firstname=None, lastname=None):
    """create a user"""
    if username:
        user = User(username)
        statement = user.post(firstname, lastname)
    else:
        statement = 'no username provided'
    return statement

@app.route("/users/delete/")
@app.route("/users/delete/<username>")
def delete_user(username=None):
    """delete a user, TODO: Unable to delete user while books are checked out"""
    if username:
        user = User(username)
        statement = user.delete()
    else:
        statement = 'username missing'
    return statement

@app.route("/books/get/")
@app.route("/books/get/<title>")
def get_book(title=None):
    """get a specific book"""
    if title:
        book = Book(title)
        statement = book.get()
    else:
        statement = 'no title provided'
    return statement

@app.route("/books/post/")
@app.route("/books/post/<title>/<year>")
def post_book(title=None, year=None, borrower=None):
    """post (create) a book"""
    if title and year:
        book = Book(title)
        statement = book.post(year, borrower)
    else:
        statement = 'invalid'
    return statement

@app.route("/books/delete/")
@app.route("/books/delete/<title>")
def delete_book(title=None):
    """# delete a book # TODO: Programmatically manipulate a book based on UUID"""
    if title:
        book = Book(title)
        statement = book.delete()
    else:
        statement = 'title missing'
    return statement

@app.route("/<collection>/")
def get_collection(collection=None):
    """Get all items in a collection"""
    statement = LIBRARY.get(collection)
    return statement

@app.route("/<collection>/reset")
def reset_collections(collection=None):
    '''Delete all items in a collection'''
    statement = LIBRARY.reset(collection)
    return statement


@app.route("/checkout/")
@app.route("/checkout/<title>/<username>")
def checkout(title=None, username=None):
    """A user checks out an available copy of a book"""
    if title and username:
        statement = LIBRARY.checkout(title, username)
    else:
        statement = 'please provide username and title'
    return statement

@app.route('/checkin/')
@app.route('/checkin/<title>/<username>')
def check_in(title=None, username=None):
    """A user checks in an available copy of a book"""
    if title and username:
        statement = LIBRARY.checkin(title, username)
    else:
        statement = 'please provide title and borrower'
    return statement

if __name__ == "__main__":
    app.run()
