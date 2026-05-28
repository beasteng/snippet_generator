"""Pass Jinja variables via dbtRunner (no CLI/subprocess)."""
import json
from dbt.cli.main import dbtRunner

runner = dbtRunner()
variables = {"execution_date": "2025-05-28", "lookback_days": 7}

res = runner.invoke(["run", "--vars", json.dumps(variables)])
print(f"Success: {res.success}")
