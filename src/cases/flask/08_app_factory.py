"""#8 — Application Factory pattern: the production-standard way to create Flask apps."""
from flask import Flask, jsonify


def create_app(config_name="development"):
    app = Flask(__name__)

    # Load config based on environment
    configs = {
        "development": {"DEBUG": True, "SECRET_KEY": "dev-secret"},
        "testing":     {"TESTING": True, "SECRET_KEY": "test-secret"},
        "production":  {"DEBUG": False, "SECRET_KEY": "prod-change-me"},
    }
    app.config.update(configs.get(config_name, configs["development"]))

    # Register routes
    @app.route("/")
    def index():
        return jsonify({
            "env": config_name,
            "debug": app.config["DEBUG"],
        })

    @app.route("/health")
    def health():
        return jsonify({"status": "ok"})

    return app


if __name__ == "__main__":
    import sys
    env = sys.argv[1] if len(sys.argv) > 1 else "development"
    app = create_app(env)
    print(f"Starting in '{env}' mode")
    app.run(port=5008)
