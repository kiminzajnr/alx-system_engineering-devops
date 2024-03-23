import requests, sys, csv

if len(sys.argv) < 2:
    print("Usage: python3 script_name.py <USER_ID>")
    sys.exit()
USER_ID = int(sys.argv[1])

todos_data = requests.get('https://jsonplaceholder.typicode.com/todos')
users_data = requests.get('https://jsonplaceholder.typicode.com/users')

USERNAME = ""

for dct in users_data.json():
    if dct.get('id') == USER_ID:
        USERNAME = dct.get('username')
        break

with open('output.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    # csvwriter.writerows(["USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"])
    for item in todos_data.json():
        # if item.get('userId'):
        csvwriter.writerow([USER_ID, USERNAME, item.get('completed'), item.get('title')])