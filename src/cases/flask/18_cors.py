"""#18 — CORS: Cross-Origin Resource Sharing headers (manual implementation)."""
from flask import Flask, jsonify, request

app = Flask(__name__)

ALLOWED_ORIGINS = ["http://localhost:3000", "https://myapp.com"]


@app.after_request
def add_cors_headers(response):
    origin = request.headers.get("Origin", "")
    if origin in ALLOWED_ORIGINS:
        response.headers["Access-Control-Allow-Origin"] = origin
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        response.headers["Access-Control-Max-Age"] = "3600"
    return response


@app.route("/api/data")
def get_data():
    return jsonify({"data": [1, 2, 3], "cors": "enabled"})


@app.route("/api/data", methods=["OPTIONS"])
def preflight():
    """Handle CORS preflight requests."""
    return "", 204


if __name__ == "__main__":
    app.run(debug=True, port=5018)
