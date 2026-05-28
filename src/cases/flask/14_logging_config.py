"""#14 — Logging: structured logging with Flask's built-in logger."""
from flask import Flask, request, jsonify
import logging
from logging.handlers import RotatingFileHandler
import os

app = Flask(__name__)


def setup_logging(app):
    """Configure file + console logging."""
    os.makedirs("logs", exist_ok=True)

    file_handler = RotatingFileHandler(
        "logs/app.log", maxBytes=100_000, backupCount=3
    )
    file_handler.setFormatter(logging.Formatter(
        "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info("Flask app started")


setup_logging(app)


@app.before_request
def log_request():
    app.logger.info(f"Request: {request.method} {request.path}")


@app.route("/")
def index():
    app.logger.info("Home page accessed")
    return jsonify({"message": "Check logs/app.log"})


@app.route("/error")
def trigger_error():
    app.logger.error("Intentional error triggered")
    return jsonify({"error": "Something went wrong"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5014)
