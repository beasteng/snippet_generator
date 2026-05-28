"""#12 — Sessions: server-side signed cookies for user state."""
from flask import Flask, session, jsonify, request

app = Flask(__name__)
app.secret_key = "super-secret-key-change-in-production"


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}
    username = data.get("username")
    if not username:
        return jsonify({"error": "Provide 'username'"}), 400
    session["username"] = username
    session["visits"] = 0
    return jsonify({"message": f"Logged in as {username}"})


@app.route("/profile")
def profile():
    if "username" not in session:
        return jsonify({"error": "Not logged in"}), 401
    session["visits"] = session.get("visits", 0) + 1
    return jsonify({
        "username": session["username"],
        "visits": session["visits"],
    })


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"message": "Logged out"})


if __name__ == "__main__":
    app.run(debug=True, port=5012)
