import requests
import time

BASE_URL = "http://your-api-url.com"  # Replace with your actual API URL

def test_post_and_get():
    tasks = ["task1", "task2", "task3"]
    
    for task in tasks:
        # Send a POST request to execute the task
        response = requests.post(f"{BASE_URL}/run?task={task}")
        assert response.status_code == 200, f"POST failed for {task}"

        # Wait for the task to complete (adjust as needed)
        time.sleep(2)  

        # Send a GET request to check the created file
        response = requests.get(f"{BASE_URL}/read?path={task}.txt")
        assert response.status_code == 200, f"GET failed for {task}"
        print(f"Test passed for {task}")

if __name__ == "__main__":
    test_post_and_get()
