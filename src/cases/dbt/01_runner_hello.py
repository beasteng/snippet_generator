"""Minimal dbtRunner invocation — run all models."""
from dbt.cli.main import dbtRunner, dbtRunnerResult

runner = dbtRunner()
res: dbtRunnerResult = runner.invoke(["run"])

print(f"Success: {res.success}")
