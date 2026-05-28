"""Run tests and inspect individual test outcomes."""
from dbt.cli.main import dbtRunner

runner = dbtRunner()
res = runner.invoke(["test"])

passed = failed = 0
for r in res.result or []:
    if r.status == "pass":
        passed += 1
    else:
        failed += 1
        print(f"❌ {r.node.unique_id}: {r.status} — {r.message}")

print(f"\n✅ {passed} passed, ❌ {failed} failed")
