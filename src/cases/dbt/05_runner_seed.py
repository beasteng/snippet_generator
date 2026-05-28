"""Load seed CSV files via Python API."""
from dbt.cli.main import dbtRunner

runner = dbtRunner()
res = runner.invoke(["seed"])

for r in res.result or []:
    print(f"Seeded: {r.node.name} ({r.execution_time:.2f}s)")
