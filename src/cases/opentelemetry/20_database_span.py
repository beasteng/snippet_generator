"""Trace database queries with db.* semantic conventions."""
import sqlite3
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    SimpleSpanProcessor(ConsoleSpanExporter())
)
tracer = trace.get_tracer(__name__)

conn = sqlite3.connect(":memory:")
with tracer.start_as_current_span("db.init", kind=trace.SpanKind.CLIENT) as span:
    span.set_attribute("db.system", "sqlite")
    conn.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT)")

sql = "INSERT INTO users VALUES (?, ?)"
with tracer.start_as_current_span("db.insert", kind=trace.SpanKind.CLIENT) as span:
    span.set_attribute("db.statement", sql)
    conn.execute(sql, (1, "Alice"))

with tracer.start_as_current_span("db.query", kind=trace.SpanKind.CLIENT) as span:
    rows = conn.execute("SELECT * FROM users").fetchall()
    span.set_attribute("db.rows_affected", len(rows))
    print(rows)
