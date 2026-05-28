"""#26 — Background Tasks: run long jobs without blocking requests."""
from flask import Flask, jsonify
import threading
import time
import uuid

app = Flask(__name__)

jobs = {}


def long_running_task(job_id: str, duration: int):
    """Simulates a long-running background task."""
    jobs[job_id]["status"] = "running"
    for i in range(duration):
        time.sleep(1)
        jobs[job_id]["progress"] = int((i + 1) / duration * 100)
    jobs[job_id]["status"] = "completed"
    jobs[job_id]["result"] = "Task finished successfully"


@app.route("/jobs", methods=["POST"])
def start_job():
    job_id = str(uuid.uuid4())[:8]
    jobs[job_id] = {"status": "queued", "progress": 0}
    thread = threading.Thread(target=long_running_task, args=(job_id, 5))
    thread.start()
    return jsonify({"job_id": job_id, "status_url": f"/jobs/{job_id}"}), 202


@app.route("/jobs/<job_id>")
def job_status(job_id):
    job = jobs.get(job_id)
    if not job:
        return jsonify({"error": "Job not found"}), 404
    return jsonify({"job_id": job_id, **job})


@app.route("/jobs")
def list_jobs():
    return jsonify(jobs)


if __name__ == "__main__":
    app.run(debug=True, port=5026)
