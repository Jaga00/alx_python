import requests
import sys
import json

def get_employee_info(employee_id):
    user_info_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_info_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    user_response = requests.get(user_info_url)
    todo_response = requests.get(todo_info_url)

    if user_response.status_code == 200 and todo_response.status_code == 200:
        user_data = user_response.json()
        todo_data = todo_response.json()

        employee_name = user_data['name']
        completed_tasks = [{"task": task['title'], "completed": task['completed'], "username": employee_name} for task in todo_data]

        with open(f"{employee_id}.json", mode='w') as file:
            json.dump({employee_id: completed_tasks}, file)

        print(f"Data exported to {employee_id}.json")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)