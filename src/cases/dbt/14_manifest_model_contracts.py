"""Inspect model contracts (column types, constraints) from manifest."""
from dbt.contracts.graph.manifest import WritableManifest
from pathlib import Path
import json

raw = json.loads(Path("target/manifest.json").read_text())
manifest = WritableManifest.from_dict(raw)

for uid, node in manifest.nodes.items():
    if node.resource_type.value == "model" and node.contract.enforced:
        print(f"\n📋 {node.name} (contract enforced)")
        for col_name, col in node.columns.items():
            constraints = [c.type.value for c in col.constraints] if col.constraints else []
            print(f"  {col_name}: {col.data_type}  constraints={constraints}")
