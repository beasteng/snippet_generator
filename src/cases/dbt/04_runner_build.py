"""dbt build = run + test + snapshot + seed in DAG order."""
from dbt.cli.main import dbtRunner

runner = dbtRunner()
res = runner.invoke(["build", "--select", "tag:core"])

for r in res.result or []:
    icon = "✅" if r.status in ("success", "pass") else "❌"
    print(f"{icon} {r.node.resource_type}: {r.node.name} → {r.status}")
