"""Complete setup: Resource, BatchSpanProcessor, Metrics, Shutdown."""
import atexit, time
from opentelemetry import trace, metrics
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import (
    ConsoleMetricExporter,
    PeriodicExportingMetricReader,
)

# ── Resource (shared by traces & metrics) ──────────────────
resource = Resource.create({
    "service.name": "interview-demo",
    "service.version": "0.1.0",
    "deployment.environment": "staging",
})

# ── Traces ─────────────────────────────────────────────────
tracer_provider = TracerProvider(resource=resource)
tracer_provider.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))
trace.set_tracer_provider(tracer_provider)
tracer = trace.get_tracer("demo")

# ── Metrics ────────────────────────────────────────────────
reader = PeriodicExportingMetricReader(ConsoleMetricExporter(), export_interval_millis=2000)
meter_provider = MeterProvider(resource=resource, metric_readers=[reader])
metrics.set_meter_provider(meter_provider)
meter = metrics.get_meter("demo")

counter = meter.create_counter("demo.requests")
histogram = meter.create_histogram("demo.latency_ms")

# ── Graceful shutdown ──────────────────────────────────────
atexit.register(tracer_provider.shutdown)
atexit.register(meter_provider.shutdown)

# ── Application logic ─────────────────────────────────────
with tracer.start_as_current_span("handle-request") as span:
    span.set_attribute("http.method", "GET")
    counter.add(1, {"http.method": "GET"})
    histogram.record(42.5, {"http.route": "/demo"})
    with tracer.start_as_current_span("db-query"):
        span.add_event("query_started")
        time.sleep(0.05)
        span.add_event("query_finished")

time.sleep(2.5)  # wait for metric export cycle
print("\n✅  Full demo complete — check console output above for traces & metrics.")
