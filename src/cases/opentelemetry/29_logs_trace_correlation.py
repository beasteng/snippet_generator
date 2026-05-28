"""Inject trace_id and span_id into Python log records."""
import logging
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    SimpleSpanProcessor(ConsoleSpanExporter())
)

class TraceInjectFilter(logging.Filter):
    def filter(self, record):
        span = trace.get_current_span()
        ctx = span.get_span_context()
        record.trace_id = f"{ctx.trace_id:#034x}" if ctx.trace_id else "0"
        record.span_id = f"{ctx.span_id:#018x}" if ctx.span_id else "0"
        return True

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(
    "%(asctime)s [trace=%(trace_id)s span=%(span_id)s] %(message)s"
))
handler.addFilter(TraceInjectFilter())

logger = logging.getLogger("app")
logger.setLevel(logging.INFO)
logger.addHandler(handler)

tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("request"):
    logger.info("processing request — trace ids in log line!")
