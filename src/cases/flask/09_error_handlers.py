"""#9 — Custom Error Handlers: return JSON for API errors, HTML for pages."""
from flask import Flask, jsonify, request

app = Flask(__name__)


class APIError(Exception):
    def __init__(self, message, status_code=400):
        self.message = message
        self.status_code = status_code


@app.errorhandler(APIError)
def handle_api_error(error):
    return jsonify({"error": error.message}), error.status_code


@app.errorhandler(404)
def not_found(error):
    if request.path.startswith("/api/"):
        return jsonify({"error": "Resource not found"}), 404
    return "<h1>404 — Page Not Found</h1>", 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500


@app.route("/api/validate", methods=["POST"])
def validate():
    data = request.get_json(silent=True) or {}
    if "email" not in data:
        raise APIError("Missing 'email' field", 422)
    return jsonify({"valid": True})


@app.route("/")
def index():
    return "<h1>Try POST /api/validate</h1>"


if __name__ == "__main__":
    app.run(debug=True, port=5009)
