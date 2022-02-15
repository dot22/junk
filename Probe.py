number = int(input('Введите количество человек: '))
family_dict = dict()
family_range = dict()
count = 1

for i_num in range(1, number):
    print(i_num, 'пара: ', end='')
    pair = input('').split(' ')
    family_dict[pair[0]] = pair[1]

family_keys = set(family_dict.keys())
family_values = set(family_dict.values())
parent = family_values.difference(family_keys)
root = parent.pop()
family_range[root] = 0

while len(family_range) != number:
    for i_fam in family_dict:
        if family_dict.get(i_fam) in family_range.keys() and i_fam not in family_range:
            family_range[i_fam] = count
    count += 1

print('\n"Высота" каждого члена семьи:')
for i_name in sorted(family_range):
    print(i_name, family_range[i_name])
