"""Register a Python callback to capture dbt log events."""
from dbt.cli.main import dbtRunner
from dbt.events.types import LogModelResult
from dbt_common.events.base_types import EventMsg

collected_events: list[EventMsg] = []

def event_callback(event: EventMsg):
    collected_events.append(event)
    # Filter only model results
    if event.info.name == "LogModelResult":
        print(f"  📦 Model finished: {event.info.msg}")

runner = dbtRunner(callbacks=[event_callback])
res = runner.invoke(["run"])

print(f"\nTotal events captured: {len(collected_events)}")
