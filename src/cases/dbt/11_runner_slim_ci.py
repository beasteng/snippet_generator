"""Slim CI: only build state-modified models using dbtRunner."""
from dbt.cli.main import dbtRunner

runner = dbtRunner()
res = runner.invoke([
    "build",
    "--select", "state:modified+",
    "--defer",
    "--state", "./prod_artifacts",
])

if res.success:
    print(f"✅ Slim CI: {len(res.result or [])} nodes processed")
else:
    print(f"❌ Slim CI failed: {res.exception}")
