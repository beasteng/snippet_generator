"""OpenTelemetry context propagates correctly inside asyncio tasks."""
import asyncio
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    SimpleSpanProcessor(ConsoleSpanExporter())
)
tracer = trace.get_tracer(__name__)

async def fetch():
    with tracer.start_as_current_span("async-fetch"):
        await asyncio.sleep(0.05)
        return 42

async def main():
    with tracer.start_as_current_span("async-main"):
        result = await fetch()
        print(result)

asyncio.run(main())
