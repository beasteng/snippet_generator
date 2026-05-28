"""Parse manifest via dbtRunner + WritableManifest dataclass."""
from dbt.cli.main import dbtRunner
from dbt.contracts.graph.manifest import WritableManifest
from pathlib import Path
import json

# First generate the manifest
runner = dbtRunner()
runner.invoke(["parse"])

# Load it as a typed dataclass
raw = json.loads(Path("target/manifest.json").read_text())
manifest = WritableManifest.from_dict(raw)

print(f"Project: {manifest.metadata.project_name}")
print(f"dbt version: {manifest.metadata.dbt_version}")
print(f"Nodes: {len(manifest.nodes)}")
print(f"Sources: {len(manifest.sources)}")
print(f"Macros: {len(manifest.macros)}")
