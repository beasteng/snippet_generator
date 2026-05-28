"""Build a structured JSON logger from dbt events (for observability)."""
from dbt.cli.main import dbtRunner
from dbt_common.events.base_types import EventMsg
import json, time

log_entries = []

def structured_logger(event: EventMsg):
    entry = {
        "ts": event.info.ts.isoformat() if event.info.ts else None,
        "level": event.info.level,
        "name": event.info.name,
        "msg": event.info.msg,
        "pid": event.info.pid,
        "thread": event.info.thread,
        "invocation_id": event.info.invocation_id,
    }
    log_entries.append(entry)

runner = dbtRunner(callbacks=[structured_logger])
start = time.time()
res = runner.invoke(["run", "--select", "tag:core"])
elapsed = time.time() - start

# Write structured logs
from pathlib import Path
Path("dbt_structured_log.jsonl").write_text(
    "\n".join(json.dumps(e) for e in log_entries)
)

print(f"Run {'succeeded' if res.success else 'failed'} in {elapsed:.1f}s")
print(f"Wrote {len(log_entries)} structured log entries to dbt_structured_log.jsonl")
