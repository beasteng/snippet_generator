"""Propagate request-scoped key-values via Baggage (not span attrs)."""
from opentelemetry import baggage, context, trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    SimpleSpanProcessor(ConsoleSpanExporter())
)
tracer = trace.get_tracer(__name__)

ctx = baggage.set_baggage("tenant.id", "acme")
ctx = baggage.set_baggage("request.priority", "high", context=ctx)

token = context.attach(ctx)
try:
    with tracer.start_as_current_span("handler") as span:
        tid = baggage.get_baggage("tenant.id")
        span.set_attribute("tenant.id", tid or "unknown")
        print(f"tenant = {tid}")
finally:
    context.detach(token)
