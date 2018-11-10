from flask import Flask
from pymongo import MongoClient

CHECKOUT_LIMIT = 3

app = Flask(__name__)
client = MongoClient('localhost', 27017)

app.debug = True

db = client.app

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
	try:
		users = db.users.find()
		statement = 'User Information: <br>'
		for user in users:
			username = user['username']
			obj_id = user['_id']
			statement = statement + f'{obj_id}: {username}<br>'
	except:
		statement = 'error'
	return statement

# get a specific user by username
@app.route("/users/get/<username>")
def get_user(username=None):
	try:
		user = db.users.find_one({'username': username})
		name = user['firstname']
		obj_id = user['_id']
		books = user['books']
		for book in books:
			book_id = book
		statement = f'{name}, {obj_id}, {book_id}'
	except:
		statement = "error"
	return statement

# create a user
@app.route("/users/post/<username>/<firstname>/<lastname>")
def post_user(username=None, firstname=None, lastname=None):
	if username and firstname and lastname:
		db.users.insert_one({
			"username": username,
			"firstname": firstname,
			"lastname": lastname,
			"books": []
		})
		statement = f'Data inserted successfully: {username}, {firstname}, {lastname}'
	else:
		statement = 'Data insufficient. Please try again!'
	return statement

# delete a user
@app.route("/users/delete/")
@app.route("/users/delete/<username>")
def delete_user(username=None):
	if username:
		try:
			db.users.remove({
				"username": username,
			})
			statement = f'{username} removed'
		except:
			statement = 'error'
	else:
		statement = 'username missing'
	return statement

### Books ###
# Get all books
@app.route("/books/")
def get_books():
	try:
		books = db.books.find()
		books_output = 'books: <br>'
		for book in books:
			title = book['title']
			year = book['year']
			borrower = book['borrower']
			books_output = books_output + (f'{title}, {year}, {borrower} <br>')
	except:
		books_output = 'an unknown error occured'
	return (''.join(books_output))

# get a specific book
@app.route("/books/get/")
@app.route("/books/get/<title>")
def get_book(title=None):
	if title:
		try:
			book = db.books.find_one({'title':title})
			year = book['year']
			borrower = book['borrower']
			statement = f'{title}, {year}, {borrower}'
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
# include a check for an borrower
@app.route("/books/delete/")
@app.route("/books/delete/<title>")
def delete_book(title=None):
	if title:
		book = db.books.find_one({"title": title})
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

## Both of these functions should only be written once
# checkout a book
@app.route("/checkout/")
@app.route("/checkout/<title>/<username>")
def checkout(title = None, username = None):
	# blank error statement
	error = []
	# check title and username are both provided; set to boolean
	if title and username:
		user = db.users.find_one({"username": username})
		book = db.books.find_one({"title": title})
		firstname = user['firstname']
		user_id = user['_id']
		year = book['year']
		book_id = book['_id']
		borrower = book['borrower']
		statement = f'{year}, {borrower}, {firstname}'

		db.books.update_one({"_id": book_id},
		{"$set":{"borrower": user_id}})

		db.users.update_one(
			{"_id": user_id},
			{
				"$push": {
					"books": book_id
				}
			}
		)
	return statement
# return a book


# @app.route("/checkout/book/")
# @app.route("/checkout/book/<title>/<owner>/")
# ## TODO: Refractor Owner to Borrower
# def checkout_book(title=None, owner=None):
# 	if title and owner:
# 		try:
# 			owner = db.user.find_one({"username": owner}) 
# 			db.books.update_one(
# 				{"title": title},
# 				{
# 					"$set":{
# 						"owner": owner
# 					}
# 				}
# 			)
# 			statement = f'/get/book/{title} to view new owner'
# 		except:
# 			statement = "Error"
# 	else:
# 		statement = "no title provided"

# 	return statement


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
