"""#10 — Middleware: before_request, after_request, teardown hooks."""
from flask import Flask, request, g, jsonify
import time
import uuid

app = Flask(__name__)


@app.before_request
def before():
    """Runs before every request — attach request ID and timer."""
    g.request_id = str(uuid.uuid4())[:8]
    g.start_time = time.perf_counter()
    print(f"  [{g.request_id}] → {request.method} {request.path}")


@app.after_request
def after(response):
    """Runs after every request — add headers and log duration."""
    duration = time.perf_counter() - g.start_time
    response.headers["X-Request-ID"] = g.request_id
    response.headers["X-Duration-Ms"] = f"{duration * 1000:.1f}"
    print(f"  [{g.request_id}] ← {response.status_code} ({duration*1000:.1f}ms)")
    return response


@app.teardown_request
def teardown(exception):
    """Runs after response is sent — cleanup resources."""
    if exception:
        print(f"  [teardown] Error occurred: {exception}")


@app.route("/")
def index():
    return jsonify({"message": "Check response headers for X-Request-ID"})


@app.route("/slow")
def slow():
    time.sleep(0.5)
    return jsonify({"message": "slow response"})


if __name__ == "__main__":
    app.run(debug=True, port=5010)
