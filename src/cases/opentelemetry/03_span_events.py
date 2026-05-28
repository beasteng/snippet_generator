"""Add timestamped events (annotations) to a span."""
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    SimpleSpanProcessor(ConsoleSpanExporter())
)
tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("payment") as span:
    span.add_event("card_validated")
    span.add_event("payment_authorized", {"auth.code": "OK"})
