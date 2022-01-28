# {
#     'server': {
#         'host': '127.0.0.1',
#         'port': '10'
#     },
#     'configuration': {
#         'ssh': {
#             'access': 'true',
#             'login': 'Ivan',
#             'password': 'qwerty'
#         }
#     }
# }

data = dict()
data['server'] = {
        'host': '127.0.0.1',
        'port': '10'
}
data['configuration'] = {
        'ssh': {
            'access': 'true',
            'login': 'Ivan',
            'password': 'qwerty'
        }
}

for i_value in data.values():
    print('i_value:', i_value)
    for j_key in i_value:
        print('j_key:', j_key)
        print('i_value_j_key:', i_value[j_key])
