## 9. Create a RESTful API using Flask to perform CRUD operations on resources like books or movies.

from flask import Flask, render_template, redirect, url_for
from flask import jsonify

app = Flask(__name__)

books = [
    {"id": 1, "title": "Abcd", "author": "PQR st"},
    {"id": 2, "title": "coder", "author": "programmer"}
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify({'book': book})
    else:
        return jsonify({'message': 'Book not found'}), 404

@app.route('/books', methods=['POST'])
def create_book():
    new_book = {'id': len(books) + 1, 'title': request.json['title'], 'author': request.json['author']}
    books.append(new_book)
    return jsonify({'book': new_book}), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        book['title'] = request.json.get('title', book['title'])
        book['author'] = request.json.get('author', book['author'])
        return jsonify({'book': book})
    else:
        return jsonify({'message': 'Book not found'}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({'message': 'Book deleted'})


if __name__ == '__main__':
    app.run(host ="0.0.0.0",port = 5002)