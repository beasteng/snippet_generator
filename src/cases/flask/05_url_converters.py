"""#5 — URL Converters: int, float, path, uuid in route parameters."""
from flask import Flask, jsonify
import uuid

app = Flask(__name__)


@app.route("/user/<int:user_id>")
def get_user(user_id):
    return jsonify({"user_id": user_id, "type": type(user_id).__name__})


@app.route("/price/<float:amount>")
def show_price(amount):
    return jsonify({"price": amount, "formatted": f"${amount:.2f}"})


@app.route("/files/<path:filepath>")
def get_file(filepath):
    return jsonify({"filepath": filepath})


@app.route("/order/<uuid:order_id>")
def get_order(order_id):
    return jsonify({"order_id": str(order_id)})


@app.route("/test-uuid")
def test_uuid():
    new_id = uuid.uuid4()
    return jsonify({"try_this_url": f"/order/{new_id}"})


if __name__ == "__main__":
    app.run(debug=True, port=5005)
