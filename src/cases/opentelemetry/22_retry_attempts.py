"""Record each retry attempt as a separate span."""
import random
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    SimpleSpanProcessor(ConsoleSpanExporter())
)
tracer = trace.get_tracer(__name__)

random.seed(0)

with tracer.start_as_current_span("operation_with_retries") as parent:
    for attempt in range(1, 6):
        with tracer.start_as_current_span(f"attempt-{attempt}") as span:
            span.set_attribute("retry.attempt", attempt)
            success = random.random() > 0.6
            span.set_attribute("retry.success", success)
            if success:
                parent.set_attribute("retry.total_attempts", attempt)
                break
