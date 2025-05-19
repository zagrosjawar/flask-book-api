# Flask Book API 📚

A Dockerized Flask REST API with a simple HTML/JS frontend to manage an online book catalog.

## 🔧 Features

- 🧾 View all books
- ➕ Add a new book
- ❌ Delete a book by ID
- 🧠 JSON-based API with full CORS support
- 💻 Web interface included (HTML/JS)
- 🐳 Packaged in a Docker container

## 🚀 Run with Docker

```bash
docker pull zagjaw/zagros-book-flask-api
docker run -p 5000:5000 zagjaw/zagros-book-flask-api

Visit your app at:
👉 http://localhost:5000


🛠️ Local Development (Without Docker)
Clone the repository:
    git clone https://github.com/zagrosjawar/flask-book-api.git
    cd flask-book-api

Set up a virtual environment and install dependencies:
    python -m venv venv
    source venv/bin/activate     # On Windows: venv\\Scripts\\activate
    pip install -r requirements.txt
Run the Flask server:
    python app.py

Visit 👉 http://localhost:5000


📁 Project Structure

flask-book-api/
├── app.py                # Main Flask API with endpoints
├── requirements.txt      # Project dependencies
├── Dockerfile            # Docker image instructions
├── .dockerignore         # Files to exclude from Docker build
├── templates/
│   └── index.html        # Web frontend (auto-served by Flask)
└── README.md             # Project documentation


🐳 Docker Support
Build the image manually (if you're working locally):
    docker build -t flask-book-api .
    docker run -p 5000:5000 flask-book-api


🧰 Built With
Flask

Flask-CORS

Docker

🧠 Author
Zagros Jawar
📎 Docker Hub
📎 GitHub




