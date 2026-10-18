from flask import Flask, jsonify, request

app = Flask(__name__)
_tasks = []
_next_id = 1


@app.get("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.get("/tasks")
def list_tasks():
    return jsonify({"tasks": _tasks}), 200


@app.post("/tasks")
def create_task():
    global _next_id

    if not request.is_json:
        return jsonify({
            "error": "invalid_content_type",
            "message": "Content-Type must be application/json"
        }), 400

    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify({
            "error": "invalid_json",
            "message": "Request body must be a JSON object"
        }), 400

    title = payload.get("title")
    if not isinstance(title, str) or not title.strip():
        return jsonify({
            "error": "validation_error",
            "message": "title is required and must be a non-empty string"
        }), 400

    task = {"id": _next_id, "title": title.strip(), "completed": False}
    _next_id += 1
    _tasks.append(task)
    return jsonify({"task": task}), 201


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
