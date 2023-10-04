import requests
import sys
import csv

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

        csv_data = []

        for task in completed_tasks:
            csv_data.append([employee_id, employee_name, task['completed'], task['title']])

        with open(f"{employee_id}.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            writer.writerows(csv_data)

        print(f"Data exported to {employee_id}.csv")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)