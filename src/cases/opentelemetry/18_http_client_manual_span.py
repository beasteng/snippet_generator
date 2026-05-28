"""Wrap an outgoing HTTP call in a CLIENT span with semantic attrs."""
import requests
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    SimpleSpanProcessor(ConsoleSpanExporter())
)
tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("http-get", kind=trace.SpanKind.CLIENT) as span:
    span.set_attribute("http.method", "GET")
    span.set_attribute("http.url", "https://httpbin.org/get")
    r = requests.get("https://httpbin.org/get", timeout=5)
    span.set_attribute("http.status_code", r.status_code)
