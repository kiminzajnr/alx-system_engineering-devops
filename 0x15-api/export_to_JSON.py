import requests, sys, json

my_lst = []
final_dict = {}

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

for item in todos_data.json():
    # if item.get('userId'):
    my_lst.append({"task": item.get('title'), "completed": item.get('completed'), "username": USERNAME})

final_dict[USER_ID] = my_lst
# print(json.dumps(final_dict, indent=4))

with open("USER_ID.json", "w", encoding='utf-8') as json_file:
    json.dump(final_dict, json_file, ensure_ascii=False, indent=4)