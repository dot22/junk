# number = int(input('Введите количество человек: '))
number = 9
# family_dict = dict()
family_dict = {'Alexei': 'Peter_I', 'Anna': 'Peter_I', 'Elizabeth': 'Peter_I', 'Peter_II': 'Alexei', 'Peter_III': 'Anna', 'Paul_I': 'Peter_III', 'Alexander_I': 'Paul_I', 'Nicholaus_I': 'Paul_I'}

family_range = dict()
count = 1

# for i_num in range(1, number):
#     print(i_num, 'пара: ', end='')
#     pair = input('').split(' ')
#     family_dict[pair[0]] = pair[1]

family_keys = set(family_dict.keys())
family_values = set(family_dict.values())
parent = family_values.difference(family_keys)
root = parent.pop()
family_range[root] = 0


# print(family_dict)
# print(family_range)
# print(family_keys)
# print(family_values)

while len(family_range) != number:
    print('len family range - ', len(family_range))
    print('family_dict', family_dict)
    for i_fam in family_dict:
        # print(i_fam)
        if family_dict.get(i_fam) in family_range.keys() and i_fam not in family_range:
            # print(i_fam, family_dict.get(i_fam), family_range.keys(), family_range)
            # print(count)
            family_range[i_fam] = count
    count += 1

print('family_range -', family_range)
#
# print('\n"Высота" каждого члена семьи:')
# for i_name in sorted(family_range):
#     print(i_name, family_range[i_name])
