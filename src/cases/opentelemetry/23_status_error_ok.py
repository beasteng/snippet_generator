"""Explicitly set span status to OK or ERROR."""
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    SimpleSpanProcessor(ConsoleSpanExporter())
)
tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("success-job") as span:
    span.set_status(trace.Status(trace.StatusCode.OK))

with tracer.start_as_current_span("failed-job") as span:
    span.set_status(trace.Status(trace.StatusCode.ERROR, "timeout"))
