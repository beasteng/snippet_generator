"""#28 — CLI Commands: custom Flask CLI with click integration."""
from flask import Flask, jsonify
import click

app = Flask(__name__)


@app.cli.command("seed")
@click.option("--count", default=5, help="Number of records to create")
def seed_db(count):
    """Seed the database with sample data."""
    for i in range(count):
        click.echo(f"  Created record {i + 1}/{count}")
    click.echo(f"Done! Seeded {count} records.")


@app.cli.command("info")
def app_info():
    """Display application information."""
    rules = [rule.rule for rule in app.url_map.iter_rules()]
    click.echo("Registered routes:")
    for r in sorted(rules):
        click.echo(f"  {r}")


@app.cli.command("health-check")
def health_check():
    """Run a quick health check."""
    with app.test_client() as client:
        resp = client.get("/health")
        if resp.status_code == 200:
            click.echo("✅ Health check passed")
        else:
            click.echo("❌ Health check failed")
            raise SystemExit(1)


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/")
def index():
    return jsonify({
        "cli_commands": [
            "flask seed --count 10",
            "flask info",
            "flask health-check",
        ],
    })


if __name__ == "__main__":
    app.run(debug=True, port=5028)
