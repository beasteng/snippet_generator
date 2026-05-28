"""#1 — Hello World: the simplest possible Flask app."""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Flask!"


@app.route("/greet/<name>")
def greet(name):
    return f"Hello, {name}!"


if __name__ == "__main__":
    app.run(debug=True, port=5001)
