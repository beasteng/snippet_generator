"""#21 — Database Migrations: schema versioning with Flask-Migrate.
   Requires: pip install flask-sqlalchemy flask-migrate"""
from flask import Flask, jsonify

try:
    from flask_sqlalchemy import SQLAlchemy
    from flask_migrate import Migrate
except ImportError:
    raise SystemExit("pip install flask-sqlalchemy flask-migrate")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///migrate_demo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # Add new columns here, then run:
    #   flask db migrate -m "description"
    #   flask db upgrade

    def to_dict(self):
        return {"id": self.id, "username": self.username, "email": self.email}


@app.route("/users")
def list_users():
    return jsonify([u.to_dict() for u in User.query.all()])


@app.route("/")
def index():
    return jsonify({
        "message": "Database migration demo",
        "commands": [
            "flask db init       # first time only",
            "flask db migrate -m 'initial'",
            "flask db upgrade",
        ],
    })


if __name__ == "__main__":
    app.run(debug=True, port=5021)
