#!/usr/bin/python3
"""
Return information for a given employee about his/her TODO list progress
"""
if __name__ == "__main__":
    import requests
    import sys

    DONE_TASKS = 0
    ALL_TASKS = 0

    URL_FOR_USERS = 'https://jsonplaceholder.typicode.com/users/{0}'.\
        format(sys.argv[1])
    URL_FOR_TODOS = 'https://jsonplaceholder.typicode.com/todos'
    r_for_users = requests.get(URL_FOR_USERS)
    r_for_todos = requests.get(URL_FOR_TODOS)

    name = r_for_users.json().get('name')
    todos = r_for_todos.json()
    for todo in todos:
        if todo.get('userId') == int(sys.argv[1]):
            ALL_TASKS += 1
        if (todo.get('userId') == int(sys.argv[1]))\
                and (todo.get('completed')):
            DONE_TASKS += 1
    print("Employee {} is done with tasks({}/{}):".
          format(name, DONE_TASKS, ALL_TASKS))
    for todo in todos:
        if (todo.get('userId') == int(sys.argv[1]))\
                and (todo.get('completed')):
            print("	 {}".format(todo.get('title')))
