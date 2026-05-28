"""Build a reverse dependency graph (children lookup) from manifest."""
from dbt.contracts.graph.manifest import WritableManifest
from pathlib import Path
from collections import defaultdict
import json

raw = json.loads(Path("target/manifest.json").read_text())
manifest = WritableManifest.from_dict(raw)

children = defaultdict(list)
for uid, node in manifest.nodes.items():
    for parent in (node.depends_on.nodes if node.depends_on else []):
        children[parent].append(uid)

# Show the most depended-upon nodes
top = sorted(children.items(), key=lambda x: -len(x[1]))[:10]
print("Top 10 most depended-upon nodes:")
for parent, kids in top:
    print(f"  {parent} → {len(kids)} downstream")
