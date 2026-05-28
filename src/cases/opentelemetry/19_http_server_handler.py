"""Simple HTTP server that creates a SERVER span per request.
   Start with: python 19_http_server_handler.py
   Test with : curl http://127.0.0.1:8080/
   Press Ctrl-C to stop.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    SimpleSpanProcessor(ConsoleSpanExporter())
)
tracer = trace.get_tracer(__name__)

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        with tracer.start_as_current_span(
            f"GET {self.path}", kind=trace.SpanKind.SERVER
        ) as span:
            span.set_attribute("http.method", "GET")
            span.set_attribute("http.target", self.path)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"ok")
            span.set_attribute("http.status_code", 200)

print("Listening on :8080 …")
HTTPServer(("127.0.0.1", 8080), Handler).serve_forever()
