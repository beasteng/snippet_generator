"""Run a single model by name via dbtRunner."""
from dbt.cli.main import dbtRunner

runner = dbtRunner()
res = runner.invoke(["run", "--select", "stg_orders"])

if res.success:
    for node_result in res.result:
        print(f"{node_result.node.unique_id} → {node_result.status}")
else:
    print("Run failed:", res.exception)
