"""Inspect semantic layer metrics defined in manifest."""
from dbt.contracts.graph.manifest import WritableManifest
from pathlib import Path
import json

raw = json.loads(Path("target/manifest.json").read_text())
manifest = WritableManifest.from_dict(raw)

metrics = manifest.metrics or {}
if not metrics:
    print("No metrics defined.")
else:
    for mid, metric in metrics.items():
        print(f"\n📏 Metric: {metric.name}")
        print(f"   Label: {metric.label}")
        print(f"   Type: {metric.type.value}")
        deps = metric.depends_on.nodes if metric.depends_on else []
        for dep in deps:
            print(f"   ← {dep}")
