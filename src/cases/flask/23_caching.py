"""#23 — Caching: in-memory cache with TTL for expensive operations."""
from flask import Flask, jsonify
import time
from functools import wraps

app = Flask(__name__)

_cache = {}


def cached(ttl_seconds=30):
    """Simple in-memory cache decorator with TTL."""
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            key = f"{f.__name__}:{args}:{kwargs}"
            now = time.time()
            if key in _cache:
                value, timestamp = _cache[key]
                if now - timestamp < ttl_seconds:
                    return value
            result = f(*args, **kwargs)
            _cache[key] = (result, now)
            return result
        return wrapper
    return decorator


@cached(ttl_seconds=10)
def expensive_query():
    """Simulates a slow database/API call."""
    time.sleep(2)
    return {"data": "computed", "timestamp": time.time()}


@app.route("/data")
def get_data():
    start = time.perf_counter()
    result = expensive_query()
    elapsed = time.perf_counter() - start
    return jsonify({**result, "response_time_ms": round(elapsed * 1000, 1)})


@app.route("/cache/clear", methods=["POST"])
def clear_cache():
    _cache.clear()
    return jsonify({"message": "Cache cleared"})


if __name__ == "__main__":
    app.run(debug=True, port=5023)
