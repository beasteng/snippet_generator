"""#7 — Blueprints: modular route organization (the Flask way to scale)."""
from flask import Flask, Blueprint, jsonify

# --- Blueprint: Users ---
users_bp = Blueprint("users", __name__, url_prefix="/users")


@users_bp.route("/")
def list_users():
    return jsonify({"users": ["alice", "bob", "charlie"]})


@users_bp.route("/<username>")
def get_user(username):
    return jsonify({"username": username})


# --- Blueprint: Products ---
products_bp = Blueprint("products", __name__, url_prefix="/products")


@products_bp.route("/")
def list_products():
    return jsonify({"products": ["widget", "gadget"]})


# --- App Factory ---
def create_app():
    app = Flask(__name__)
    app.register_blueprint(users_bp)
    app.register_blueprint(products_bp)

    @app.route("/")
    def index():
        return jsonify({
            "endpoints": ["/users/", "/users/<name>", "/products/"]
        })

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5007)
