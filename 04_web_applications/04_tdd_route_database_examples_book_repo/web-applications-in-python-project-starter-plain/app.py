import os
from lib.database_connection import get_flask_database_connection
from flask import Flask, request
from lib.book_repository import BookRepository
from lib.book import Book

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/books', methods=['GET'])
def get_books():
    connection = get_flask_database_connection(app)
    repository = BookRepository(connection)
    books = repository.all()
    book_strings = [f"{book}" for book in books]
    return "\n".join(book_strings)
    
@app.route("/books/<id>", methods = ['GET'])
def get_book(id):
    connection = get_flask_database_connection(app)
    repository = BookRepository(connection)
    book = repository.find(id)
    return str(book)

@app.route('/books', methods = ['POST'])
def post_books():
    connection = get_flask_database_connection(app)
    repository = BookRepository(connection)
    title = request.form['title']
    author_name = request.form['author_name']
    book = Book(None, title, author_name )
    repository.create(book)
    return "Book created successfully."

@app.route('/books/<id>', methods = ['DELETE'])
def delete_books(id):
    connection = get_flask_database_connection(app)
    repository = BookRepository(connection)
    repository.delete(id)
    return 'Book successfully removed'

@app.route('/books/<id>', methods = ['PATCH'])
def patch_book(id):
    connection = get_flask_database_connection(app)
    repository = BookRepository(connection)
    title = request.form['title']
    author_name = request.form['author_name']
    repository.update(id, title, author_name)
    repository.all()
    return f"Book {id} has been updated"
    


# == Example Code Below ==


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

