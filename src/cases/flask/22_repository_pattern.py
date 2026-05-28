"""#22 — Repository Pattern: separate data access from route logic."""
from flask import Flask, request, jsonify

app = Flask(__name__)


# --- Repository Layer ---
class TaskRepository:
    def __init__(self):
        self._tasks = {}
        self._counter = 0

    def get_all(self) -> list[dict]:
        return list(self._tasks.values())

    def get_by_id(self, task_id: int) -> dict | None:
        return self._tasks.get(task_id)

    def create(self, title: str) -> dict:
        self._counter += 1
        task = {"id": self._counter, "title": title, "done": False}
        self._tasks[self._counter] = task
        return task

    def update(self, task_id: int, **fields) -> dict | None:
        task = self._tasks.get(task_id)
        if task:
            task.update(fields)
        return task

    def delete(self, task_id: int) -> bool:
        return self._tasks.pop(task_id, None) is not None


repo = TaskRepository()


# --- Routes (thin controllers) ---
@app.route("/tasks", methods=["GET"])
def list_tasks():
    return jsonify(repo.get_all())


@app.route("/tasks", methods=["POST"])
def create_task():
    title = (request.get_json(silent=True) or {}).get("title", "Untitled")
    return jsonify(repo.create(title)), 201


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json(silent=True) or {}
    task = repo.update(task_id, **data)
    return jsonify(task) if task else (jsonify({"error": "Not found"}), 404)


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    if repo.delete(task_id):
        return jsonify({"deleted": task_id})
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    app.run(debug=True, port=5022)
