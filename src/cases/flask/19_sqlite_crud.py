"""#19 — SQLite CRUD: full Create/Read/Update/Delete with raw SQL."""
from flask import Flask, request, jsonify, g
import sqlite3

app = Flask(__name__)
DATABASE = "flask_crud.db"


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(exc):
    db = g.pop("db", None)
    if db:
        db.close()


def init_db():
    with app.app_context():
        db = get_db()
        db.execute("""
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                done BOOLEAN DEFAULT 0
            )
        """)
        db.commit()


@app.route("/todos", methods=["GET"])
def list_todos():
    rows = get_db().execute("SELECT * FROM todos").fetchall()
    return jsonify([dict(r) for r in rows])


@app.route("/todos", methods=["POST"])
def create_todo():
    data = request.get_json(silent=True) or {}
    title = data.get("title", "Untitled")
    db = get_db()
    cur = db.execute("INSERT INTO todos (title) VALUES (?)", (title,))
    db.commit()
    return jsonify({"id": cur.lastrowid, "title": title, "done": False}), 201


@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    data = request.get_json(silent=True) or {}
    db = get_db()
    db.execute(
        "UPDATE todos SET title=?, done=? WHERE id=?",
        (data.get("title", ""), data.get("done", False), todo_id),
    )
    db.commit()
    row = db.execute("SELECT * FROM todos WHERE id=?", (todo_id,)).fetchone()
    return jsonify(dict(row)) if row else (jsonify({"error": "Not found"}), 404)


@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    db = get_db()
    db.execute("DELETE FROM todos WHERE id=?", (todo_id,))
    db.commit()
    return jsonify({"deleted": todo_id})


if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5019)
