"""#20 — SQLAlchemy ORM: models, relationships, and queries.
   Requires: pip install flask-sqlalchemy"""
from flask import Flask, jsonify, request

try:
    from flask_sqlalchemy import SQLAlchemy
except ImportError:
    raise SystemExit("pip install flask-sqlalchemy")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///orm_demo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    books = db.relationship("Book", backref="author", lazy=True)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "book_count": len(self.books)}


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"), nullable=False)

    def to_dict(self):
        return {"id": self.id, "title": self.title, "author": self.author.name}


with app.app_context():
    db.create_all()


@app.route("/authors", methods=["POST"])
def create_author():
    name = (request.get_json(silent=True) or {}).get("name")
    if not name:
        return jsonify({"error": "name required"}), 400
    author = Author(name=name)
    db.session.add(author)
    db.session.commit()
    return jsonify(author.to_dict()), 201


@app.route("/authors")
def list_authors():
    return jsonify([a.to_dict() for a in Author.query.all()])


@app.route("/books", methods=["POST"])
def create_book():
    data = request.get_json(silent=True) or {}
    book = Book(title=data.get("title", "Untitled"), author_id=data.get("author_id"))
    db.session.add(book)
    db.session.commit()
    return jsonify(book.to_dict()), 201


@app.route("/books")
def list_books():
    return jsonify([b.to_dict() for b in Book.query.all()])


if __name__ == "__main__":
    app.run(debug=True, port=5020)
