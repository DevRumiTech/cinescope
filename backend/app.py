from flask import Flask, jsonify, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

MOVIES = [
    {
        "id": 1,
        "title": "Inception",
        "genre": "Sci-Fi",
        "score": 9.1
    },
    {
        "id": 2,
        "title": "Interstellar",
        "genre": "Sci-Fi",
        "score": 9.0
    },
    {
        "id": 3,
        "title": "The Matrix",
        "genre": "Sci-Fi",
        "score": 8.9
    },
    {
        "id": 4,
        "title": "The Dark Knight",
        "genre": "Action",
        "score": 9.2
    },
    {
        "id": 5,
        "title": "Mad Max: Fury Road",
        "genre": "Action",
        "score": 8.7
    },
    {
        "id": 6,
        "title": "Parasite",
        "genre": "Thriller",
        "score": 8.8
    },
    {
        "id": 7,
        "title": "Fight Club",
        "genre": "Drama",
        "score": 8.7
    },
    {
        "id": 8,
        "title": "Blade Runner 2049",
        "genre": "Sci-Fi",
        "score": 8.6
    },
    {
        "id": 9,
        "title": "Joker",
        "genre": "Drama",
        "score": 8.5
    },
    {
        "id": 10,
        "title": "Se7en",
        "genre": "Thriller",
        "score": 8.6
    }
]

@app.route("/api/movies", methods=["GET"])
def get_movies():
    """
    Query params:
    - genre: filter by genre
    - search: search by title
    """
    genre = request.args.get("genre", "").lower()
    search = request.args.get("search", "").lower()

    results = MOVIES

    if genre:
        results = [m for m in results if m["genre"].lower() == genre]

    if search:
        results = [m for m in results if search in m["title"].lower()]

    # Sort by recommendation score (highest first)
    results = sorted(results, key=lambda x: x["score"], reverse=True)

    return jsonify(results)

@app.route("/api/surprise", methods=["GET"])
def surprise_movie():
    """
    Returns a single random movie recommendation
    """
    return jsonify(random.choice(MOVIES))

@app.route("/api/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)
