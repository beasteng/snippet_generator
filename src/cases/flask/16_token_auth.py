"""#16 — Token Auth: Bearer token authentication with decorators."""
from flask import Flask, request, jsonify
from functools import wraps
import hashlib
import time

app = Flask(__name__)
app.secret_key = "change-me"

# Simple token store (use Redis/DB in production)
tokens = {}


def generate_token(username):
    raw = f"{username}:{time.time()}:{app.secret_key}"
    token = hashlib.sha256(raw.encode()).hexdigest()
    tokens[token] = {"username": username, "created": time.time()}
    return token


def require_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization", "")
        if not auth_header.startswith("Bearer "):
            return jsonify({"error": "Missing Bearer token"}), 401
        token = auth_header.split(" ", 1)[1]
        user_data = tokens.get(token)
        if not user_data:
            return jsonify({"error": "Invalid token"}), 401
        request.current_user = user_data["username"]
        return f(*args, **kwargs)
    return decorated


@app.route("/auth/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}
    username = data.get("username")
    password = data.get("password")
    if username == "admin" and password == "secret":
        token = generate_token(username)
        return jsonify({"token": token})
    return jsonify({"error": "Invalid credentials"}), 401


@app.route("/auth/me")
@require_token
def me():
    return jsonify({"user": request.current_user})


if __name__ == "__main__":
    app.run(debug=True, port=5016)
