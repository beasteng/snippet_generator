"""#2 — HTTP Methods: GET, POST, PUT, DELETE on the same resource."""
from flask import Flask, request, jsonify

app = Flask(__name__)

items = []


@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)


@app.route("/items", methods=["POST"])
def create_item():
    data = request.get_json()
    items.append(data)
    return jsonify(data), 201


@app.route("/items/<int:index>", methods=["PUT"])
def update_item(index):
    if 0 <= index < len(items):
        items[index] = request.get_json()
        return jsonify(items[index])
    return jsonify({"error": "Not found"}), 404


@app.route("/items/<int:index>", methods=["DELETE"])
def delete_item(index):
    if 0 <= index < len(items):
        removed = items.pop(index)
        return jsonify(removed)
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    app.run(debug=True, port=5002)
