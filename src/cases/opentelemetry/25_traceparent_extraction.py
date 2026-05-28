"""Extract W3C traceparent from incoming headers and continue the trace."""
from opentelemetry import propagate, trace, context
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    SimpleSpanProcessor(ConsoleSpanExporter())
)
tracer = trace.get_tracer(__name__)

# Simulate incoming headers from an upstream service
incoming = {
    "traceparent": "00-0af7651916cd43dd8448eb211c80319c-b7ad6b7169203331-01"
}

ctx = propagate.extract(incoming)
token = context.attach(ctx)
try:
    with tracer.start_as_current_span("receiver") as span:
        print(f"Parent trace id: {span.get_span_context().trace_id:#034x}")
finally:
    context.detach(token)
