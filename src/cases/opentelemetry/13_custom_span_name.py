"""Use dynamic span names that match HTTP route patterns."""
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    SimpleSpanProcessor(ConsoleSpanExporter())
)
tracer = trace.get_tracer(__name__)

# GOOD:  use the route template, not the concrete path
method, route = "GET", "/users/{id}"
with tracer.start_as_current_span(f"{method} {route}") as span:
    span.set_attribute("http.method", method)
    span.set_attribute("http.route", route)
