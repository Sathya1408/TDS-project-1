import requests
import time

BASE_URL = "http://localhost:5000"

def post_task(task_name):
    """Send a POST request to /run?task=..."""
    url = f"{BASE_URL}/run?task={task_name}"
    response = requests.post(url)
    print(f"POST {url} -> Status: {response.status_code}, Response: {response.text}")
    return response

def get_file(path):
    """Send a GET request to /read?path=..."""
    url = f"{BASE_URL}/read?path={path}"
    response = requests.get(url)
    print(f"GET {url} -> Status: {response.status_code}, Response: {response.text}")
    return response

# Test cases
if __name__ == "__main__":
    task_names = ["task1", "task2", "task3"]

    # Call POST /run for multiple tasks
    for task in task_names:
        post_task(task)
        time.sleep(1)  # Wait a bit before the next request

    # Check if the correct files are created
    file_paths = ["output/task1.txt", "output/task2.txt", "output/task3.txt"]
    for path in file_paths:
        get_file(path)
