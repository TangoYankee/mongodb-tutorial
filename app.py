from flask import Flask
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
client = MongoClient('localhost', 27017)

app.debug = True

db = client.app

# default routing provies reference to all routes
@app.route("/")
def index():
	return 'Please follow links to make use of Mongo Database: <br>' \
		'1. /get/ - get all users <br>' \
		'3. /username/ - get particular user <br>' \
		'2. /delete/username/ - delete user with username <br>' \
		'3. /insert/username/firstname/lastname/ - insert user <br>' \

@app.route("/get/book/")
@app.route("/get/book/<title>")
def get_book(title=None):
	if title:
		try:
			book = db.books.find_one({'title':title})
			year = book['year']
			owner = book['owner']
			statement = f'{title}, {year}, {owner}'
		except:
			statement = 'an error occurred'
	else:
		statement = 'no title provided'
	return statement

@app.route("/get/all-books/")
def get_all_books():
	try:
		books = db.books.find()
		book_list = []
		for book in books:
			title = book['title']
			year = book['year']
			owner = book['owner']
			book_list.append(f'{title}, {year}, {owner} <br>')
	except:
		book_list = 'an unknown error occured'

	return (''.join(book_list))

# getting all registered user data
# e.g. http://localhost:5000/get/
@app.route("/get/")
def get_data():
	users = db.users.find()
	data = 'Name of Users: <br>'
	for user in users:
		data = data + user['username'] + ': ' \
		+ user['firstname'] + user['lastname'] + '<br>'
	return data

@app.route("/post/book/")
@app.route("/post/book/<title>/<year>/<owner>")
def insert_book(title=None, year=None, owner=None):
	if title and year:
		# The books collection is started automatically
		obj_id = ObjectId()
		db.books.insert_one({
			"obj_id": obj_id, 
			"title": title,
			"year": year,
			"owner": owner
		})
		statement = (f'{title}, {year}')
	else:
		statement = 'invalid'
	return statement

@app.route("/checkout/book/")
@app.route("/checkout/book/<title>/<owner>/")
## TODO: Refractor Owner to Borrower
def checkout_book(title=None, owner=None):
	if title and owner:
		try:
			owner = db.user.find_one({"username": owner}) 
			db.books.update_one(
				{"title": title},
				{
					"$set":{
						"owner": owner
					}
				}
			)
			statement = f'/get/book/{title} to view new owner'
		except:
			statement = "Error"
	else:
		statement = "no title provided"

	return statement

# insert user with username, firstname and password
# e.g. http://localhost:5000/insert/jeevan/Jeevan/Pant/
@app.route("/insert/")
@app.route("/insert/<username>/<firstname>/<lastname>/")
# variables still need to be passed to through the function
# setting it equal none does not override the value passed
def insert_data(username=None, firstname=None, lastname=None):
	if username and firstname and lastname:
		obj_id = ObjectId()
		db.users.insert_one({
			"obj_id": obj_id,
			"username": username,
			"firstname": firstname,
			"lastname": lastname,
		})
		return f'Data inserted successfully: {obj_id}, {username}, {firstname}, {lastname}'
	else:
		return 'Data insufficient. Please try again!'

# delete user
# e.g. http://localhost:5000/remove/jeevan/Jeevan/Pant/
# @app.route("/insert/") Adding this line means that this URL will also direct to this function
@app.route("/delete/")
@app.route("/delete/<username>/")
def delete_data(username=None):
	if username != None:
		db.users.remove({
			"username": username,
		})
		return 'Data delected successfully with useraname: ' +  username
	else:
		return 'Provide data to delete. Please try again!'

# get specific user
# e.g. http://localhost:5000/jeevan/
@app.route("/get-user/<username>/")
def users(username):
	try:
		user = db.users.find_one({'username': username})
		name = user['firstname']
		obj_id = user['_id']
		return f'{name}, {obj_id}'
	except:
		return "User couldn't be found"

if __name__ == "__main__":
    app.run()