"""Automatic parent-child relationship via nested context managers."""
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    SimpleSpanProcessor(ConsoleSpanExporter())
)
tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("request"):
    with tracer.start_as_current_span("validate"):
        print("validating…")
    with tracer.start_as_current_span("save"):
        print("saving…")
