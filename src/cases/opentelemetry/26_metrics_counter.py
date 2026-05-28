"""Create a monotonic counter metric."""
import time
from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import (
    ConsoleMetricExporter,
    PeriodicExportingMetricReader,
)

reader = PeriodicExportingMetricReader(ConsoleMetricExporter(), export_interval_millis=1000)
metrics.set_meter_provider(MeterProvider(metric_readers=[reader]))
meter = metrics.get_meter(__name__)

request_counter = meter.create_counter(
    name="http.server.requests",
    description="Total HTTP requests",
    unit="1",
)

request_counter.add(1, {"http.method": "GET", "http.route": "/users"})
request_counter.add(1, {"http.method": "POST", "http.route": "/users"})

time.sleep(1.5)  # wait for periodic export
