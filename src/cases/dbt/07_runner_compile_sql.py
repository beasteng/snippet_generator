"""Compile a model to see the rendered SQL (no execution)."""
from dbt.cli.main import dbtRunner

runner = dbtRunner()
res = runner.invoke(["compile", "--select", "fct_revenue"])

if res.success and res.result:
    for r in res.result:
        print(f"-- {r.node.unique_id}")
        print(r.node.compiled_code)
