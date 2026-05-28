"""Aggregate materialization strategies across all models."""
from dbt.contracts.graph.manifest import WritableManifest
from pathlib import Path
from collections import Counter
import json

raw = json.loads(Path("target/manifest.json").read_text())
manifest = WritableManifest.from_dict(raw)

stats = Counter()
for node in manifest.nodes.values():
    if node.resource_type.value == "model":
        stats[node.config.materialized] += 1

print("Materialization breakdown:")
for mat, count in stats.most_common():
    bar = "█" * count
    print(f"  {mat:15s} {count:3d}  {bar}")
