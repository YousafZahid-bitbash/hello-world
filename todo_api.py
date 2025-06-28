from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple in-memory storage for tasks
tasks = []

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Todo API",
        "endpoints": {
            "GET /tasks": "Get all tasks",
            "POST /tasks": "Add a new task",
            "PUT /tasks/<id>/complete": "Mark task as complete",
            "DELETE /tasks/<id>": "Delete a task"
        }
    })

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    if not data or 'task' not in data:
        return jsonify({"error": "Task description is required"}), 400
    
    new_task = {
        "id": len(tasks) + 1,
        "task": data['task'],
        "completed": False
    }
    tasks.append(new_task)
    return jsonify({"message": "Task added successfully", "task": new_task}), 201

@app.route('/tasks/<int:task_id>/complete', methods=['PUT'])
def complete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            return jsonify({"message": "Task marked as complete", "task": task})
    
    return jsonify({"error": "Task not found"}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            deleted_task = tasks.pop(i)
            return jsonify({"message": "Task deleted", "task": deleted_task})
    
    return jsonify({"error": "Task not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000) 