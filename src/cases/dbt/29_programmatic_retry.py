"""Retry only failed nodes from the previous dbt run (no subprocess)."""
from dbt.cli.main import dbtRunner
from dbt.contracts.results import RunResultsArtifact
from pathlib import Path
import json

MAX_RETRIES = 3

runner = dbtRunner()

for attempt in range(1, MAX_RETRIES + 1):
    print(f"\n🔄 Attempt {attempt}/{MAX_RETRIES}")

    if attempt == 1:
        res = runner.invoke(["run"])
    else:
        # Use result_path from previous run — retry only failures
        res = runner.invoke(["run", "--select", "result:fail", "result:error",
                             "--state", "target"])

    if res.success:
        print("✅ All nodes succeeded!")
        break

    # Inspect what failed
    raw = json.loads(Path("target/run_results.json").read_text())
    results = RunResultsArtifact.from_dict(raw)
    failed = [r for r in results.results if r.status in ("error", "fail")]
    print(f"   {len(failed)} node(s) failed")
    for f in failed:
        print(f"   ❌ {f.unique_id}: {f.status}")

else:
    print(f"\n💀 Still failing after {MAX_RETRIES} attempts")
    raise SystemExit(1)
