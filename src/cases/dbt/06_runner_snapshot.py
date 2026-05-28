"""Execute dbt snapshots (SCD Type 2) via Python API."""
from dbt.cli.main import dbtRunner

runner = dbtRunner()
res = runner.invoke(["snapshot"])

for r in res.result or []:
    print(f"Snapshot: {r.node.name} → {r.status} ({r.execution_time:.2f}s)")
