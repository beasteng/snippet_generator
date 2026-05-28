"""Parse catalog.json (typed) to audit column types across all models."""
from dbt.contracts.results import CatalogArtifact
from pathlib import Path
from collections import Counter
import json

raw = json.loads(Path("target/catalog.json").read_text())
catalog = CatalogArtifact.from_dict(raw)

type_counts = Counter()
total_cols = 0

for table_id, table in catalog.nodes.items():
    for col_name, col in table.columns.items():
        type_counts[col.type] += 1
        total_cols += 1

print(f"Total columns across catalog: {total_cols}")
print(f"\nColumn type distribution:")
for dtype, count in type_counts.most_common(15):
    pct = 100 * count / total_cols
    print(f"  {dtype:<25} {count:>5}  ({pct:.1f}%)")
