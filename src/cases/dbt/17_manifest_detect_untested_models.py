"""Identify models lacking tests via manifest API (data governance)."""
from dbt.contracts.graph.manifest import WritableManifest
from pathlib import Path
import json

raw = json.loads(Path("target/manifest.json").read_text())
manifest = WritableManifest.from_dict(raw)

# Collect all models referenced by tests
tested = set()
for node in manifest.nodes.values():
    if node.resource_type.value == "test":
        for dep in (node.depends_on.nodes if node.depends_on else []):
            tested.add(dep)

untested = [
    n.name for n in manifest.nodes.values()
    if n.resource_type.value == "model" and n.unique_id not in tested
]

print(f"⚠️  {len(untested)} model(s) without tests:")
for name in sorted(untested):
    print(f"  • {name}")
