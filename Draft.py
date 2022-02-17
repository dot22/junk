# number = int(input('Введите количество человек: '))
number = 9
family_dict = dict()
family_dict = {'Alexei': 'Peter_I', 'Anna': 'Peter_I', 'Elizabeth': 'Peter_I', 'Peter_II': 'Alexei', 'Peter_III': 'Anna', 'Paul_I': 'Peter_III', 'Alexander_I': 'Paul_I', 'Nicholaus_I': 'Paul_I'}
# family_dict = {'8': '7', '7': '6', '6': '5', '5': '4', '4': '3', '3': '2', '2': '1'}
family_range = dict()
count = 0

# for i_num in range(1, number):
#     print(i_num, 'пара: ', end='')
#     pair = input('').split(' ')
#     family_dict[pair[0]] = pair[1]

family_keys = set(family_dict.keys())
family_values = set(family_dict.values())
parent = family_values.difference(family_keys)
root = parent.pop()
family_range[root] = count


# print(family_dict)
# print(family_range)
# print(family_keys)
# print(family_values)

while len(family_dict) != 0:
    # print('len family range - ', len(family_range))
    # print('family_dict', family_dict)
    for i_fam in family_dict:
        if (family_dict.get(i_fam) in family_range) and not (i_fam in family_range):
            print(i_fam, family_dict.get(i_fam))
            family_range[i_fam] = count + 1
            print(family_range[i_fam])
    count += 1

print('family_range -', family_range)

print('\n"Высота" каждого члена семьи:')
for i_name in sorted(family_range):
    print(i_name, family_range[i_name])
