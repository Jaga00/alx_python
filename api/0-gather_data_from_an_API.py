import requests
import sys

def get_employee_info(employee_id):
    user_info_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_info_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    user_response = requests.get(user_info_url)
    todo_response = requests.get(todo_info_url)

    if user_response.status_code == 200 and todo_response.status_code == 200:
        user_data = user_response.json()
        todo_data = todo_response.json()

        employee_name = user_data['name']
        completed_tasks = [task for task in todo_data if task['completed']]
        total_tasks = len(todo_data)

        print(f"Employee {employee_name} is done with tasks ({len(completed_tasks)}/{total_tasks}):")

        for task in completed_tasks:
            print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)