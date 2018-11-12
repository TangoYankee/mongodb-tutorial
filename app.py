from flask import Flask
from pymongo import MongoClient, ReturnDocument
from validators import User, AllUsers

CHECKOUT_LIMIT = 3

app = Flask(__name__)
client = MongoClient('localhost', 27017)

app.debug = True

db = client.mongodb_tutorial
## Home

# default routing provies reference to all routes
@app.route("/")
def index():
	return 'Please follow links to make use of Mongo Database: <br>' \
		'1. /users/ - get all users <br>' \
		'2. /users/username/ - get particular user <br>' \

### Users ###
# Get all users
@app.route("/users/")
def get_users():
	users = AllUsers()
	statement = users.get
	return statement

# get a specific user by username
@app.route("/users/get/")
@app.route("/users/get/<username>")
def get_user(username=None):
	if username:
		user = User(username)
		statement = user.get()
	else:
		statement = 'please provide a username'
	return statement

# create a user
## TODO: Make username a unique field. Replace user_id with username as key from book to user
@app.route("/users/post/<username>/<firstname>/<lastname>")
def post_user(username=None, firstname=None, lastname=None):
	if username:
		user = User(username)
		statement = user.post(firstname, lastname)
	else:
		statement = 'no username provided'

	return statement

# delete a user
# TODO: Unable to delete user while books are checked out
@app.route("/users/delete/")
@app.route("/users/delete/<username>")
def delete_user(username=None):
	if username:
		user = User(username)
		statement = user.delete()
	else:
		statement = 'username missing'
	return statement

### Books ###
# Get all books
@app.route("/books/")
def get_books():
	try:
		books = db.books.find()
		statement = ''
		for book in books:
			statement = statement + (f'{book}<br>')
	except:
		statement = 'an unknown error occured'
	return statement

# get a specific book
@app.route("/books/get/")
@app.route("/books/get/<title>")
def get_book(title=None):
	if title:
		try:
			books = db.books.find({'title':title})
			statement = ''
			for book in books:
				statement = statement + f'{book}<br>'
		except:
			statement = 'an error occurred'
	else:
		statement = 'no title provided'
	return statement

# post (create) a book
@app.route("/books/post/")
@app.route("/books/post/<title>/<year>")
def post_book(title=None, year=None, borrower=None):
	if title and year:
		# The books collection is started automatically
		db.books.insert_one({ 
			"title": title,
			"year": year,
			"borrower": borrower
		})
		statement = (f'{title}, {year}, {borrower}')
	else:
		statement = 'invalid'
	return statement

# delete a book
# TODO: Programmatically manipulate a book based on UUID
# include a check for an borrower
@app.route("/books/delete/")
@app.route("/books/delete/<title>")
def delete_book(title=None):
	if title:
		book = db.books.find_one({"title": title}, {'borrower': 1})
		borrower = book['borrower']
		if not borrower:
			try:
				db.books.remove({
					"title": title,
				})
				statement = f'{title} removed'
			except:
				statement = 'error'
		else:
			statement = f'this book is checkout by {borrower} and cannot be deleted'
	else:
		statement = 'title missing'
	return statement

# checkout a book
@app.route("/checkout/")
@app.route("/checkout/<title>/<username>")
def checkout(title = None, username = None):
	if title and username:
		try:
			book = db.books.find_one_and_update(
									{'$and': [
										{ 'title' : title },
										{ 'borrower': None}]},
									{'$set' : 
										{"borrower": username}},
									return_document=ReturnDocument.AFTER	
									)
			book_id = book['_id']
			user = db.users.update_one(
				{"username": username},
				{"$push": 
					{"books": book_id}
				}
			)
			statement = f'Book: {book} <br> {user}'
		except:
			statement = 'error'
	else:
		statement = 'please provide username and title'
	return statement

# checkin a book
@app.route('/checkin/')
@app.route('/checkin/<title>/<username>')
def check_in(title=None, username=None):
	if title and username:
		try:
			book = db.books.find_one_and_update({'$and': [
								{ 'title' : title },
								{ 'borrower': username}]},
							{'$set' : 
								{"borrower": None}},
							return_document=ReturnDocument.AFTER)
			book_id = book['_id']
			user = db.users.update_one(
				{"username": username},
				{"$pull": {"books": book_id}})
			statement = f'Book: {book} <br> User: {user}'
		except:
			statement = 'error'
	else:
		statement = 'please provide title and borrower'
	return statement
	

@app.route("/users/reset")
def reset_users():
	try:
		db.users.remove()
		statement = 'users reset'
	except:
		statement = 'error'
	return statement

@app.route("/books/reset")
def reset_books():
	try:
		db.books.remove()
		statement = 'books reset'
	except:
		statement = 'error'
	return statement

if __name__ == "__main__":
    app.run()
