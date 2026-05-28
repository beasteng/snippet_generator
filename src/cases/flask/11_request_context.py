"""#11 — Request Context & g object: share data within a request lifecycle."""
from flask import Flask, g, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = ":memory:"


def get_db():
    """Get or create a DB connection for the current request."""
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
        g.db.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, text TEXT)")
        g.db.execute("INSERT OR IGNORE INTO notes VALUES (1, 'Hello from SQLite')")
        g.db.commit()
    return g.db


@app.teardown_appcontext
def close_db(exception):
    """Close DB connection when request ends."""
    db = g.pop("db", None)
    if db is not None:
        db.close()


@app.route("/notes")
def list_notes():
    db = get_db()
    rows = db.execute("SELECT * FROM notes").fetchall()
    return jsonify([dict(r) for r in rows])


@app.route("/notes", methods=["POST"])
def add_note():
    db = get_db()
    text = (request.get_json(silent=True) or {}).get("text", "empty")
    db.execute("INSERT INTO notes (text) VALUES (?)", (text,))
    db.commit()
    return jsonify({"status": "created", "text": text}), 201


if __name__ == "__main__":
    app.run(debug=True, port=5011)
