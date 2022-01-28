# family_member = {
#     "name": "Jane",
#     "surname": "Doe",
#     "hobbies": ["running", "sky diving", "singing"],
#     "age": 35,
#     "children": [
#         {
#             "name": "Alice",
#             "age": 6
#         },
#         {
#             "name": "Bob",
#             "age": 8
#         }
#     ]
# }
# print(family_member)

family_member = dict()
family_member['name'] = 'Jane'
family_member['surname'] = 'Doe'
family_member['hobbies'] = ['running', 'sky diving', 'singing']
family_member['age'] = 35
family_member['children'] = [
    {
        'name': 'Alice',
        'age': 6
    },
    {
        'name': 'Bob',
        'age': 8
    }
]

for i_children in family_member['children']:
    if i_children.get('name', 'Noname') == 'Bob':
        print('Есть ребенок с именем Bob')
    print(i_children.get('name': 'Bob', 'Noname') == 'Rob':
        print(i_children.get('name'))
