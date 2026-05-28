"""#25 — Server-Sent Events (SSE): real-time streaming without WebSocket."""
from flask import Flask, Response, jsonify
import time
import json

app = Flask(__name__)


def event_stream():
    """Generator that yields SSE-formatted events."""
    count = 0
    while count < 10:
        count += 1
        data = json.dumps({"count": count, "time": time.time()})
        yield f"id: {count}\ndata: {data}\n\n"
        time.sleep(1)
    yield "event: close\ndata: stream ended\n\n"


@app.route("/stream")
def stream():
    return Response(
        event_stream(),
        mimetype="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


@app.route("/")
def index():
    return """
    <h2>SSE Demo</h2>
    <div id="events"></div>
    <script>
        const es = new EventSource("/stream");
        es.onmessage = (e) => {
            document.getElementById("events").innerHTML += "<p>" + e.data + "</p>";
        };
        es.addEventListener("close", () => { es.close(); });
    </script>
    """


if __name__ == "__main__":
    app.run(debug=True, port=5025, threaded=True)
