"""
Complete dbt orchestration pipeline — 100% Python API.

Steps:
  1. Parse project & validate
  2. Install packages
  3. Seed static data
  4. Run models (with retry)
  5. Test
  6. Source freshness
  7. Generate docs
  8. Analyze manifest for governance
  9. Emit structured run report
"""
from dbt.cli.main import dbtRunner, dbtRunnerResult
from dbt.contracts.results import RunResultsArtifact
from dbt.contracts.graph.manifest import WritableManifest
from dbt_common.events.base_types import EventMsg
from pathlib import Path
from collections import Counter
import json, time, sys


class DbtOrchestrator:
    def __init__(self):
        self.events: list[dict] = []
        self.runner = dbtRunner(callbacks=[self._capture_event])
        self.start_time = time.time()

    def _capture_event(self, event: EventMsg):
        self.events.append({
            "ts": event.info.ts.isoformat() if event.info.ts else None,
            "level": event.info.level,
            "name": event.info.name,
            "msg": event.info.msg,
        })

    def step(self, label: str, args: list[str]) -> dbtRunnerResult:
        print(f"\n{'='*60}")
        print(f"  STEP: {label}")
        print(f"  dbt {' '.join(args)}")
        print(f"{'='*60}")
        res = self.runner.invoke(args)
        status = "✅" if res.success else "❌"
        print(f"{status} {label}: {'success' if res.success else 'FAILED'}")
        return res

    def run_with_retry(self, args: list[str], retries: int = 3) -> dbtRunnerResult:
        for attempt in range(1, retries + 1):
            res = self.runner.invoke(args)
            if res.success:
                print(f"  ✅ Succeeded on attempt {attempt}")
                return res
            print(f"  ⚠️ Attempt {attempt}/{retries} failed")
            if attempt < retries:
                time.sleep(5)
                args_retry = ["run", "--select", "result:fail", "result:error",
                              "--state", "target"]
                args = args_retry  # next attempt retries only failures
        return res

    def governance_check(self):
        print(f"\n{'='*60}")
        print("  GOVERNANCE CHECK")
        print(f"{'='*60}")

        manifest_path = Path("target/manifest.json")
        if not manifest_path.exists():
            print("  ⚠️ No manifest found, skipping")
            return

        raw = json.loads(manifest_path.read_text())
        manifest = WritableManifest.from_dict(raw)

        # Check 1: Untested models
        tested = set()
        for node in manifest.nodes.values():
            if node.resource_type.value == "test":
                for dep in (node.depends_on.nodes if node.depends_on else []):
                    tested.add(dep)

        untested = [
            n.name for n in manifest.nodes.values()
            if n.resource_type.value == "model" and n.unique_id not in tested
        ]
        if untested:
            print(f"  ⚠️ {len(untested)} untested models: {untested[:5]}...")

        # Check 2: Materialization distribution
        mats = Counter(
            n.config.materialized for n in manifest.nodes.values()
            if n.resource_type.value == "model"
        )
        print(f"  📊 Materializations: {dict(mats)}")

        # Check 3: Total lineage depth indicator
        model_count = sum(1 for n in manifest.nodes.values()
                          if n.resource_type.value == "model")
        source_count = len(manifest.sources)
        print(f"  📦 {model_count} models, {source_count} sources")

    def timing_report(self):
        results_path = Path("target/run_results.json")
        if not results_path.exists():
            return

        raw = json.loads(results_path.read_text())
        results = RunResultsArtifact.from_dict(raw)

        slowest = sorted(results.results, key=lambda r: r.execution_time, reverse=True)[:5]
        print(f"\n  🐢 Slowest nodes:")
        for r in slowest:
            name = r.unique_id.split(".")[-1]
            print(f"     {name}: {r.execution_time:.2f}s ({r.status})")

    def emit_report(self):
        elapsed = time.time() - self.start_time
        report = {
            "elapsed_total": round(elapsed, 2),
            "total_events": len(self.events),
            "error_events": sum(1 for e in self.events if e["level"] == "error"),
        }
        Path("dbt_pipeline_report.json").write_text(json.dumps(report, indent=2))
        print(f"\n📄 Report written to dbt_pipeline_report.json")
        print(f"   Total time: {elapsed:.1f}s | Events: {report['total_events']}")

    def run_pipeline(self):
        self.step("Parse & validate",     ["parse"])
        self.step("Install packages",     ["deps"])
        self.step("Load seeds",           ["seed"])

        res = self.run_with_retry(["run"], retries=3)
        if not res.success:
            print("❌ Models failed after retries — aborting")
            sys.exit(1)

        self.step("Run tests",            ["test"])
        self.step("Source freshness",     ["source", "freshness"])
        self.step("Generate docs",        ["docs", "generate"])

        self.governance_check()
        self.timing_report()
        self.emit_report()

        print("\n🎉 Pipeline complete!")


if __name__ == "__main__":
    DbtOrchestrator().run_pipeline()
