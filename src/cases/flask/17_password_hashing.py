"""#17 — Password Hashing: secure password storage with werkzeug."""
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Simulated user store
user_db = {}


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json(silent=True) or {}
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Provide username and password"}), 400
    if username in user_db:
        return jsonify({"error": "User already exists"}), 409

    user_db[username] = {
        "password_hash": generate_password_hash(password),
    }
    return jsonify({"message": f"User '{username}' registered"}), 201


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}
    username = data.get("username")
    password = data.get("password")

    user = user_db.get(username)
    if not user or not check_password_hash(user["password_hash"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    return jsonify({"message": f"Welcome back, {username}!"})


@app.route("/users")
def list_users():
    """Shows usernames only — never expose password hashes!"""
    return jsonify({"users": list(user_db.keys())})


if __name__ == "__main__":
    app.run(debug=True, port=5017)
