from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Directory to store task outputs
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# POST /run?task=...
@app.route('/run', methods=['POST'])
def run_task():
    task = request.args.get('task')
    if not task:
        return jsonify({"error": "Task parameter is missing"}), 400
    
    output_file = os.path.join(OUTPUT_DIR, f"{task}.txt")
    with open(output_file, "w") as f:
        f.write(f"Task {task} executed successfully.")
    
    return jsonify({"message": f"Task {task} created", "path": output_file})

# GET /read?path=...
@app.route('/read', methods=['GET'])
def read_task():
    path = request.args.get('path')
    if not path or not os.path.exists(path):
        return jsonify({"error": "Invalid or missing path"}), 400

    with open(path, "r") as f:
        content = f.read()

    return jsonify({"task_output": content})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
