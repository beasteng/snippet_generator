"""#3 — JSON API: request parsing, validation, structured responses."""
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/api/echo", methods=["POST"])
def echo():
    """Echo back whatever JSON is sent."""
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid or missing JSON"}), 400
    return jsonify({"received": data, "keys": list(data.keys())})


@app.route("/api/calculate", methods=["POST"])
def calculate():
    """Simple calculator API with input validation."""
    data = request.get_json(silent=True) or {}
    a = data.get("a")
    b = data.get("b")
    op = data.get("op", "add")

    if a is None or b is None:
        return jsonify({"error": "Provide 'a' and 'b'"}), 400

    ops = {
        "add": a + b,
        "sub": a - b,
        "mul": a * b,
        "div": a / b if b != 0 else "division by zero",
    }

    if op not in ops:
        return jsonify({"error": f"Unknown op: {op}"}), 400

    return jsonify({"result": ops[op], "op": op})


if __name__ == "__main__":
    app.run(debug=True, port=5003)
