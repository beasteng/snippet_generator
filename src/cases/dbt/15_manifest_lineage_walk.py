"""Walk the full DAG lineage for a model (all ancestors)."""
from dbt.contracts.graph.manifest import WritableManifest
from pathlib import Path
import json

raw = json.loads(Path("target/manifest.json").read_text())
manifest = WritableManifest.from_dict(raw)

def get_all_ancestors(manifest, node_id, visited=None):
    if visited is None:
        visited = set()
    node = manifest.nodes.get(node_id) or manifest.sources.get(node_id)
    if not node:
        return visited
    for parent_id in getattr(node, "depends_on", None) and node.depends_on.nodes or []:
        if parent_id not in visited:
            visited.add(parent_id)
            get_all_ancestors(manifest, parent_id, visited)
    return visited

TARGET = "model.my_project.fct_revenue"
ancestors = get_all_ancestors(manifest, TARGET)
print(f"Ancestors of {TARGET}:")
for a in sorted(ancestors):
    print(f"  ← {a}")
