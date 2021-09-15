#!/usr/bin/python3
"""
export data in JSON format
Records all tasks from all employees
"""
if __name__ == "__main__":
    import json
    import requests

    FILENAME = 'todo_all_employees.json'
    URL_FOR_USERS = 'https://jsonplaceholder.typicode.com/users'
    URL_FOR_TODOS = 'https://jsonplaceholder.typicode.com/todos'

    r_for_users = requests.get(URL_FOR_USERS)
    r_for_todos = requests.get(URL_FOR_TODOS)

    users = r_for_users.json()
    todos = r_for_todos.json()
    print(len(users))
    with open(FILENAME, 'w+') as f:
        for user in users:
            json.dump({user.get("id"): [{
                "username": user.get("username"),
                "task": todo.get("title"),
                "completed": todo.get("completed")} for todo in todos]}, f)
