"""Manually attach a span to the context (useful for frameworks)."""
from opentelemetry import trace, context
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    SimpleSpanProcessor(ConsoleSpanExporter())
)
tracer = trace.get_tracer(__name__)

span = tracer.start_span("manual-parent")
ctx = trace.set_span_in_context(span)
token = context.attach(ctx)
try:
    with tracer.start_as_current_span("manual-child"):
        pass
finally:
    context.detach(token)
    span.end()
