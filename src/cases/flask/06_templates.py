"""#6 — Jinja2 Templates: render HTML with dynamic data."""
from flask import Flask, render_template_string

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html>
<head><title>{{ title }}</title></head>
<body>
    <h1>{{ title }}</h1>
    <ul>
    {% for item in items %}
        <li>{{ item.name }} — ${{ "%.2f"|format(item.price) }}</li>
    {% endfor %}
    </ul>
    {% if items|length == 0 %}
        <p>No items found.</p>
    {% endif %}
</body>
</html>
"""


@app.route("/")
def shop():
    items = [
        {"name": "Widget", "price": 9.99},
        {"name": "Gadget", "price": 24.50},
        {"name": "Doohickey", "price": 4.75},
    ]
    return render_template_string(TEMPLATE, title="My Shop", items=items)


if __name__ == "__main__":
    app.run(debug=True, port=5006)
