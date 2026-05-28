"""Track cache hit/miss ratio via span attributes."""
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    SimpleSpanProcessor(ConsoleSpanExporter())
)
tracer = trace.get_tracer(__name__)
_cache: dict = {}

def get_user(user_id: int) -> dict:
    with tracer.start_as_current_span("cache.get_user") as span:
        span.set_attribute("user.id", user_id)
        if user_id in _cache:
            span.set_attribute("cache.hit", True)
            return _cache[user_id]
        span.set_attribute("cache.hit", False)
        user = {"id": user_id, "name": f"user-{user_id}"}
        _cache[user_id] = user
        return user

print(get_user(1))  # miss
print(get_user(1))  # hit
