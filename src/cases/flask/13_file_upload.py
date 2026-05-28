"""#13 — File Upload: accept, validate, and save uploaded files."""
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["MAX_CONTENT_LENGTH"] = 2 * 1024 * 1024  # 2MB limit

ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "csv"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    f = request.files["file"]
    if f.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if not allowed_file(f.filename):
        return jsonify({"error": f"Allowed types: {ALLOWED_EXTENSIONS}"}), 400

    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
    path = os.path.join(app.config["UPLOAD_FOLDER"], f.filename)
    f.save(path)
    return jsonify({"message": "Uploaded", "path": path, "size": os.path.getsize(path)})


@app.route("/")
def index():
    return """
    <h2>Upload a File</h2>
    <form method="POST" action="/upload" enctype="multipart/form-data">
        <input type="file" name="file">
        <button type="submit">Upload</button>
    </form>
    """


if __name__ == "__main__":
    app.run(debug=True, port=5013)
