"""Sample ~20 % of traces based on trace-id hash (deterministic)."""
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.sampling import TraceIdRatioBased
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

trace.set_tracer_provider(
    TracerProvider(sampler=TraceIdRatioBased(0.2))
)
trace.get_tracer_provider().add_span_processor(
    SimpleSpanProcessor(ConsoleSpanExporter())
)
tracer = trace.get_tracer(__name__)

for i in range(10):
    with tracer.start_as_current_span(f"req-{i}"):
        pass
