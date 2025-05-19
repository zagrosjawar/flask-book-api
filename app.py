import flask
from flask_cors import CORS
from flask import Flask, request, jsonify, render_template

app = Flask(__name__) # this file is where the app lives
CORS(app)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {
        "id": 1,
        "isbn": "9781593279509",
        "title": "Eloquent JavaScript, Third Edition",
        "subtitle": "A Modern Introduction to Programming",
        "author": "Marijn Haverbeke",
        "published": "2018-12-04T00:00:00.000Z",
        "publisher": "No Starch Press",
        "pages": 472,
        "description": "JavaScript lies at the heart of almost every modern web application, from social apps like Twitter to browser-based game frameworks like Phaser and Babylon...",
        "website": "http://eloquentjavascript.net/"
    },
    {
        "id": 2,
        "isbn": "9781491943533",
        "title": "Practical Modern JavaScript",
        "subtitle": "Dive into ES6 and the Future of JavaScript",
        "author": "Nicolás Bevacqua",
        "published": "2017-07-16T00:00:00.000Z",
        "publisher": "O'Reilly Media",
        "pages": 334,
        "description": "To get the most out of modern JavaScript, you need to learn the latest features of its parent specification, ECMAScript 6 (ES6)...",
        "website": "https://github.com/mjavascript/practical-modern-javascript"
    }
]

# Create a URL route in our application for "/"
@app.route("/", methods=["GET"]) # this is the root endpoint; the starting point of the API; hme page; 
def home():
    return render_template("index.html")


# API endpoint to return all books
@app.route("/api/v1/books/all", methods=["GET"]) # this is the endpoint for getting all books
def api_all_books():
    return jsonify(books)

@app.route("/api/v1/books/<int:book_id>", methods=["GET"]) # this is the endpoint for getting a book by id
                                                           # URL looks like: 👉 GET /api/v1/books/1
def api_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

# Add a new book
@app.route("/api/v1/books", methods=["POST"])
def add_book():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()

    required_fields = {"id", "isbn", "title", "subtitle", "author", "published", "publisher", "pages", "description", "website"}
    if not required_fields.issubset(data.keys()):
        return jsonify({"error": f"Missing required fields: {required_fields - data.keys()}"}), 400

    if any(book["id"] == data["id"] for book in books):
        return jsonify({"error": "Book with this ID already exists"}), 400

    books.append(data)
    return jsonify({"message": "Book added successfully", "book": data}), 201


# ✅ Now this is correctly defined as a separate route
@app.route("/api/v1/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)

    if not book:
        return jsonify({"error": "Book not found"}), 404

    books.remove(book)
    return jsonify({"message": f"Book with ID {book_id} has been deleted."}), 200




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)


'''
✅ I've created a complete professional **frontend interface** for your Flask book API using plain HTML, CSS, and JavaScript. It allows users to:

* View all books
* Add a new book
* Delete a book by ID

The interface uses `fetch()` to interact with your existing API endpoints.

Let me know if you’d like to:

* Add **edit/update functionality**
* Convert this into a **React app**
* Make it look better with **Bootstrap or Tailwind**
* Package it into the same Docker container as your Flask API
'''