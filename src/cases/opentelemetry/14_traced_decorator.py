"""Reusable decorator that wraps any function in a span."""
from functools import wraps
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    SimpleSpanProcessor(ConsoleSpanExporter())
)
tracer = trace.get_tracer(__name__)

def traced(func):
    @wraps(func)
    def wrapper(*a, **kw):
        with tracer.start_as_current_span(func.__qualname__):
            return func(*a, **kw)
    return wrapper

@traced
def business_logic():
    return "ok"

print(business_logic())
