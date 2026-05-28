"""Inject W3C traceparent header into an outgoing carrier (dict)."""
from opentelemetry import propagate, trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    SimpleSpanProcessor(ConsoleSpanExporter())
)
tracer = trace.get_tracer(__name__)

headers: dict[str, str] = {}
with tracer.start_as_current_span("sender"):
    propagate.inject(headers)

print("Outgoing headers:", headers)
# → {'traceparent': '00-<trace_id>-<span_id>-01'}
