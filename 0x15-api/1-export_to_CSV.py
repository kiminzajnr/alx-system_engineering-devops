#!/usr/bin/python3
"""
Return information for a given employee about his/her TODO list progress
"""
if __name__ == "__main__":
    import csv
    import requests
    import sys

    DONE_TASKS = 0
    ALL_TASKS = 0
    csvList = []

    URL_FOR_USERS = 'https://jsonplaceholder.typicode.com/users/{0}'.\
        format(sys.argv[1])
    URL_FOR_TODOS = 'https://jsonplaceholder.typicode.com/todos'
    r_for_users = requests.get(URL_FOR_USERS)
    r_for_todos = requests.get(URL_FOR_TODOS)

    name = r_for_users.json().get('name')
    user_name = r_for_users.json().get('username')
    todos = r_for_todos.json()
    for todo in todos:
        if todo.get('userId') == int(sys.argv[1]):
            subcsvList = []
        if todo.get('userId') == int(sys.argv[1]):
            ALL_TASKS += 1
            subcsvList.append(todo.get('userId'))
            subcsvList.append(user_name)
            subcsvList.append(todo.get('completed'))
            subcsvList.append(todo.get('title'))
            csvList.append(subcsvList)
        if (todo.get('userId') == int(sys.argv[1]))\
                and (todo.get('completed')):
            DONE_TASKS += 1
    with open(sys.argv[1] + '.csv', 'w+', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(csvList)
