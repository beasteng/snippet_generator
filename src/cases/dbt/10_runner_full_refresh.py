"""Full refresh incremental models via dbtRunner."""
from dbt.cli.main import dbtRunner

runner = dbtRunner()
res = runner.invoke([
    "run",
    "--select", "tag:incremental",
    "--full-refresh",
])

for r in res.result or []:
    print(f"{r.node.name}: {r.status} ({r.execution_time:.2f}s)")
