"""#27 — Testing: write and run tests with Flask's test client.
   Run with: python -m pytest 27_testing.py -v"""
from flask import Flask, jsonify, request


def create_app():
    app = Flask(__name__)
    items = []

    @app.route("/items", methods=["GET"])
    def get_items():
        return jsonify(items)

    @app.route("/items", methods=["POST"])
    def add_item():
        data = request.get_json(silent=True) or {}
        if "name" not in data:
            return jsonify({"error": "name required"}), 400
        items.append(data)
        return jsonify(data), 201

    @app.route("/health")
    def health():
        return jsonify({"status": "ok"})

    return app


# ─── Tests (run with pytest) ───

import pytest


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "ok"


def test_get_items_empty(client):
    resp = client.get("/items")
    assert resp.status_code == 200
    assert resp.get_json() == []


def test_create_item(client):
    resp = client.post("/items", json={"name": "Widget"})
    assert resp.status_code == 201
    assert resp.get_json()["name"] == "Widget"


def test_create_item_missing_name(client):
    resp = client.post("/items", json={})
    assert resp.status_code == 400


def test_items_persist_in_request(client):
    client.post("/items", json={"name": "A"})
    client.post("/items", json={"name": "B"})
    resp = client.get("/items")
    assert len(resp.get_json()) == 2


if __name__ == "__main__":
    # Also runnable as a Flask app
    app = create_app()
    app.run(debug=True, port=5027)
