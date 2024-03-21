import requests, sys


todos_data = requests.get('https://jsonplaceholder.typicode.com/todos')
users_data = requests.get('https://jsonplaceholder.typicode.com/users')

if len(sys.argv) < 2:
    print("Usage: python3 script_name.py <USER_ID>")
    sys.exit()
else:
    USER_ID = int(sys.argv[1])

TITLES = ""
EMPLOYEE_NAME = ""
NUMBER_OF_DONE_TASKS = 0
NUMBER_OF_UNDONE_TASKS = 0


for dct in users_data.json():
    if dct.get('id') == USER_ID:
        EMPLOYEE_NAME = dct.get('name')

for item in todos_data.json():
    if item.get('userId') == USER_ID and item.get('completed') == True:
        NUMBER_OF_DONE_TASKS += 1
        TITLES += "     " + item.get('title') + "\n"
    else:
        if item.get('userId') == USER_ID and item.get('completed') == False:
           NUMBER_OF_UNDONE_TASKS += 1 

TOTAL_NUMBER_OF_TASKS = NUMBER_OF_DONE_TASKS + NUMBER_OF_UNDONE_TASKS

print(f"Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS})")
print(TITLES)