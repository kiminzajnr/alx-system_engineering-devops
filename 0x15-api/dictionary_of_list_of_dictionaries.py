import requests, sys, json

# my_lst = []
final_dict = {}

todos_data = requests.get('https://jsonplaceholder.typicode.com/todos')
users_data = requests.get('https://jsonplaceholder.typicode.com/users')


for dct in users_data.json():
    my_lst = []
    for item in todos_data.json():
        my_lst.append({"task": item.get('title'), "completed": item.get('completed'), "username": dct.get('username')})
    final_dict[dct.get('id')] = my_lst

# print(json.dumps(final_dict, indent=4))
# final_dict[USER_ID] = my_lst
# print(json.dumps(final_dict, indent=4))

with open("todo_all_employees.json", "w", encoding='utf-8') as json_file:
    json.dump(final_dict, json_file, ensure_ascii=False, indent=4)