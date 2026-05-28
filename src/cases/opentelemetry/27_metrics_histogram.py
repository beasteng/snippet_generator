"""Record latency distribution with a Histogram."""
import time, random
from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import (
    ConsoleMetricExporter,
    PeriodicExportingMetricReader,
)

reader = PeriodicExportingMetricReader(ConsoleMetricExporter(), export_interval_millis=1000)
metrics.set_meter_provider(MeterProvider(metric_readers=[reader]))
meter = metrics.get_meter(__name__)

latency = meter.create_histogram("http.server.duration", unit="ms")

for _ in range(20):
    latency.record(random.uniform(5, 500), {"http.route": "/search"})

time.sleep(1.5)
