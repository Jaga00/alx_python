import requests
import json

def get_all_employees_info():
    all_users_url = "https://jsonplaceholder.typicode.com/users"
    all_todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_response = requests.get(all_users_url)
    todos_response = requests.get(all_todos_url)

    if users_response.status_code == 200 and todos_response.status_code == 200:
        users_data = users_response.json()
        todos_data = todos_response.json()

        all_employees_info = {}

        for user in users_data:
            employee_id = user['id']
            employee_name = user['name']
            employee_todos = [{"username": employee_name, "task": task['title'], "completed": task['completed']} for task in todos_data if task['userId'] == employee_id]

            all_employees_info[employee_id] = employee_todos

        with open("todo_all_employees.json", mode='w') as file:
            json.dump(all_employees_info, file)

        print("Data exported to todo_all_employees.json")

if __name__ == "__main__":
    get_all_employees_info()