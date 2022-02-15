number = int(input('Введите количество человек: '))
family_dict = dict()
family_range = dict()
count = 0

for i_num in range(1, number):
    print(i_num, 'пара: ', end='')
    pair = input('').split(' ')
    print(pair)
    family_dict[pair[0]] = pair[1]

family_keys = set(family_dict.keys())
family_values = set(family_dict.values())
parent = family_values.difference(family_keys)
print('parent', parent)

while True:
    family_range[parent] = count