"""Spans created in threads are independent — context does NOT auto-propagate."""
from concurrent.futures import ThreadPoolExecutor
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    SimpleSpanProcessor(ConsoleSpanExporter())
)
tracer = trace.get_tracer(__name__)

def work(ctx):
    """Manually pass context to threads for correct parenting."""
    from opentelemetry import context as ctx_mod
    token = ctx_mod.attach(ctx)
    try:
        with tracer.start_as_current_span("thread-work"):
            return 1
    finally:
        ctx_mod.detach(token)

from opentelemetry import context as ctx_mod

with tracer.start_as_current_span("parent"):
    ctx = ctx_mod.get_current()
    with ThreadPoolExecutor(max_workers=2) as pool:
        fut = pool.submit(work, ctx)
        print(fut.result())
