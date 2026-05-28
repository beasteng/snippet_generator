"""UpDownCounter tracks values that can go up AND down (e.g. in-flight)."""
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

in_flight = meter.create_up_down_counter("http.server.active_requests")

in_flight.add(1)
in_flight.add(1)
in_flight.add(-1)  # one finished

time.sleep(1.5)
