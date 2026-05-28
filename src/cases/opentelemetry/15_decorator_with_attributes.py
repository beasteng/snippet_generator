"""Decorator that also records argument count and return value type."""
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
        with tracer.start_as_current_span(func.__qualname__) as span:
            span.set_attribute("code.args_count", len(a) + len(kw))
            result = func(*a, **kw)
            span.set_attribute("code.return_type", type(result).__name__)
            return result
    return wrapper

@traced
def add(a: int, b: int) -> int:
    return a + b

print(add(2, 3))
