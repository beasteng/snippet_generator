"""#24 — Rate Limiting: protect endpoints from abuse (manual implementation)."""
from flask import Flask, request, jsonify
from functools import wraps
import time
from collections import defaultdict

app = Flask(__name__)

# Sliding window rate limiter
request_log = defaultdict(list)


def rate_limit(max_requests=5, window_seconds=60):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            client_ip = request.remote_addr
            now = time.time()

            # Remove old entries outside the window
            request_log[client_ip] = [
                t for t in request_log[client_ip]
                if now - t < window_seconds
            ]

            if len(request_log[client_ip]) >= max_requests:
                retry_after = window_seconds - (now - request_log[client_ip][0])
                return jsonify({
                    "error": "Rate limit exceeded",
                    "retry_after_seconds": round(retry_after, 1),
                }), 429

            request_log[client_ip].append(now)
            return f(*args, **kwargs)
        return wrapper
    return decorator


@app.route("/api/limited")
@rate_limit(max_requests=3, window_seconds=30)
def limited_endpoint():
    return jsonify({"message": "Success", "ip": request.remote_addr})


@app.route("/api/unlimited")
def unlimited_endpoint():
    return jsonify({"message": "No rate limit here"})


if __name__ == "__main__":
    app.run(debug=True, port=5024)
