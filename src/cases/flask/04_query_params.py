"""#4 — Query Parameters: filtering, pagination, defaults."""
from flask import Flask, request, jsonify

app = Flask(__name__)

BOOKS = [
    {"id": i, "title": f"Book {i}", "genre": ["fiction", "science", "history"][i % 3]}
    for i in range(50)
]


@app.route("/books")
def list_books():
    """GET /books?genre=fiction&page=1&per_page=10"""
    genre = request.args.get("genre")
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)

    filtered = BOOKS if not genre else [b for b in BOOKS if b["genre"] == genre]

    start = (page - 1) * per_page
    end = start + per_page
    paginated = filtered[start:end]

    return jsonify({
        "data": paginated,
        "page": page,
        "per_page": per_page,
        "total": len(filtered),
    })


if __name__ == "__main__":
    app.run(debug=True, port=5004)
