"""Execute raw SQL via dbt's adapter connection (no external driver)."""
from dbt.cli.main import dbtRunner
from dbt.adapters.factory import get_adapter, register_adapter
from dbt.config.runtime import RuntimeConfig
from dbt.mp_context import get_mp_context
import dbt.flags as flags

# Step 1: parse the project to get config
runner = dbtRunner()
runner.invoke(["parse"])

# Step 2: use the adapter to run arbitrary SQL
# NOTE: This is an advanced pattern — adapter must already be registered
# In practice you access it inside a dbt macro or custom materialization.
# Below is a conceptual example:
from pathlib import Path
import json

manifest = json.loads(Path("target/manifest.json").read_text())
adapter_type = manifest["metadata"]["adapter_type"]
print(f"Adapter type: {adapter_type}")
print("To execute raw SQL, use adapter.execute() inside dbt context")
print("or use dbtRunner with run-operation for ad-hoc queries.")
