"""#29 — API Versioning: support multiple API versions simultaneously."""
from flask import Flask, Blueprint, jsonify

# --- V1 API ---
v1 = Blueprint("v1", __name__, url_prefix="/api/v1")


@v1.route("/users")
def v1_users():
    return jsonify({
        "version": "v1",
        "users": [
            {"name": "Alice"},
            {"name": "Bob"},
        ],
    })


# --- V2 API (enhanced response format) ---
v2 = Blueprint("v2", __name__, url_prefix="/api/v2")


@v2.route("/users")
def v2_users():
    return jsonify({
        "version": "v2",
        "data": {
            "users": [
                {"id": 1, "name": "Alice", "email": "alice@example.com"},
                {"id": 2, "name": "Bob", "email": "bob@example.com"},
            ],
        },
        "meta": {"total": 2, "page": 1},
    })


# --- App Factory ---
def create_app():
    app = Flask(__name__)
    app.register_blueprint(v1)
    app.register_blueprint(v2)

    @app.route("/")
    def index():
        return jsonify({
            "available_versions": {
                "v1": "/api/v1/users",
                "v2": "/api/v2/users",
            },
            "latest": "v2",
        })

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5029)
