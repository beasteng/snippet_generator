"""#30 — Production-Ready App: combines factory, blueprints, error handling,
   middleware, config, health check, and graceful patterns into one file."""
from flask import Flask, Blueprint, jsonify, request, g
import time
import os
import logging

# ─── Config ───
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-change-me")
    DEBUG = False

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    pass

CONFIGS = {"development": DevConfig, "production": ProdConfig}

# ─── Blueprint: API ───
api = Blueprint("api", __name__, url_prefix="/api")

_store = {"items": []}

@api.route("/items", methods=["GET"])
def list_items():
    return jsonify({"data": _store["items"], "count": len(_store["items"])})

@api.route("/items", methods=["POST"])
def create_item():
    data = request.get_json(silent=True) or {}
    if "name" not in data:
        return jsonify({"error": "name is required"}), 400
    item = {"id": len(_store["items"]) + 1, "name": data["name"]}
    _store["items"].append(item)
    return jsonify(item), 201

# ─── Blueprint: Health ───
health_bp = Blueprint("health", __name__)

@health_bp.route("/health")
def health():
    return jsonify({"status": "ok", "uptime": time.time() - g.get("app_start", 0)})

@health_bp.route("/ready")
def ready():
    return jsonify({"ready": True})

# ─── Factory ───
def create_app(env=None):
    env = env or os.environ.get("FLASK_ENV", "development")
    app = Flask(__name__)
    app.config.from_object(CONFIGS.get(env, DevConfig))

    # Logging
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s: %(message)s",
    )

    # Middleware
    @app.before_request
    def before():
        g.start_time = time.perf_counter()
        g.app_start = getattr(app, "_start_time", time.time())

    @app.after_request
    def after(response):
        duration = (time.perf_counter() - g.start_time) * 1000
        response.headers["X-Response-Time"] = f"{duration:.1f}ms"
        app.logger.info(
            f"{request.method} {request.path} → {response.status_code} ({duration:.1f}ms)"
        )
        return response

    # Error handlers
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"error": "Not found"}), 404

    @app.errorhandler(500)
    def server_error(e):
        return jsonify({"error": "Internal server error"}), 500

    # Register blueprints
    app.register_blueprint(api)
    app.register_blueprint(health_bp)

    @app.route("/")
    def index():
        return jsonify({
            "app": "Flask Masterclass — Production App",
            "env": env,
            "endpoints": [
                "GET  /health",
                "GET  /ready",
                "GET  /api/items",
                "POST /api/items",
            ],
        })

    app._start_time = time.time()
    app.logger.info(f"App created in '{env}' mode")
    return app


if __name__ == "__main__":
    import sys
    env = sys.argv[1] if len(sys.argv) > 1 else "development"
    app = create_app(env)
    app.run(port=5030)
