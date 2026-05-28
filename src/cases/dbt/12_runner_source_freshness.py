"""Check source freshness entirely from Python."""
from dbt.cli.main import dbtRunner

runner = dbtRunner()
res = runner.invoke(["source", "freshness"])

for r in res.result or []:
    status_icon = "🟢" if r.status == "pass" else "🔴"
    print(f"{status_icon} {r.node.unique_id} → {r.status}")
