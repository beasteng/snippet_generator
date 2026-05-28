"""#15 — Basic Auth: simple username/password authentication decorator."""
from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)

USERS = {"admin": "secret123", "user": "pass456"}


def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or USERS.get(auth.username) != auth.password:
            return jsonify({"error": "Unauthorized"}), 401, {
                "WWW-Authenticate": 'Basic realm="Login Required"'
            }
        return f(*args, **kwargs)
    return decorated


@app.route("/public")
def public():
    return jsonify({"message": "This is public"})


@app.route("/protected")
@require_auth
def protected():
    return jsonify({
        "message": "Welcome to the protected area",
        "user": request.authorization.username,
    })


if __name__ == "__main__":
    app.run(debug=True, port=5015)
