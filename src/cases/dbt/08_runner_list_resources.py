"""List all resources (models, tests, sources) without running them."""
from dbt.cli.main import dbtRunner

runner = dbtRunner()
res = runner.invoke(["ls", "--output", "json", "--resource-type", "model"])

# res.result is a list of JSON strings when output=json
import json
for item in res.result or []:
    node = json.loads(item) if isinstance(item, str) else item
    print(f"{node.get('name', node)} — {node.get('config', {}).get('materialized', '?')}")
