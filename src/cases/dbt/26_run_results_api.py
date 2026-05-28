"""Parse run_results.json into typed dataclass + build timing report."""
from dbt.contracts.results import RunResultsArtifact
from pathlib import Path
import json

raw = json.loads(Path("target/run_results.json").read_text())
results = RunResultsArtifact.from_dict(raw)

print(f"Total elapsed: {results.elapsed_time:.2f}s")
print(f"dbt version:   {results.metadata.dbt_version}")
print()

# Sort by execution time (slowest first)
sorted_results = sorted(results.results, key=lambda r: r.execution_time, reverse=True)

print(f"{'Node':<50} {'Status':<10} {'Time':>8}")
print("-" * 70)
for r in sorted_results[:15]:
    name = r.unique_id.split(".")[-1]
    print(f"{name:<50} {r.status:<10} {r.execution_time:>7.2f}s")
