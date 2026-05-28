"""Capture an exception inside a span and mark it as ERROR."""
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    SimpleSpanProcessor(ConsoleSpanExporter())
)
tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("divide") as span:
    try:
        1 / 0
    except ZeroDivisionError as exc:
        span.record_exception(exc)
        span.set_status(trace.Status(trace.StatusCode.ERROR, "division by zero"))
