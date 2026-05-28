"""Invoke a custom macro (run-operation) via Python API."""
from dbt.cli.main import dbtRunner
import json

runner = dbtRunner()

# Example: call a macro named "grant_select" with arguments
res = runner.invoke([
    "run-operation", "grant_select",
    "--args", json.dumps({"schema": "analytics", "role": "reporter"})
])

if res.success:
    print("✅ Macro executed successfully")
else:
    print(f"❌ Macro failed: {res.exception}")
