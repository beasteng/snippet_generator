"""Find all models that feed into exposures (dashboards, ML, etc.)."""
from dbt.contracts.graph.manifest import WritableManifest
from pathlib import Path
import json

raw = json.loads(Path("target/manifest.json").read_text())
manifest = WritableManifest.from_dict(raw)

for exp_id, exposure in manifest.exposures.items():
    deps = exposure.depends_on.nodes if exposure.depends_on else []
    print(f"\n📊 Exposure: {exposure.name} (type={exposure.type.value})")
    print(f"   Owner: {exposure.owner.name}")
    for dep in deps:
        print(f"   ← {dep}")
