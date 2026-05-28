"""Child function automatically inherits parent span context."""
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    SimpleSpanProcessor(ConsoleSpanExporter())
)
tracer = trace.get_tracer(__name__)

def child_work():
    with tracer.start_as_current_span("child"):
        print("child sees parent automatically")

with tracer.start_as_current_span("parent"):
    child_work()
