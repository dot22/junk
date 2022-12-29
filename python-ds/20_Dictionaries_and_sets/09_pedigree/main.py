number = int(input('Введите количество человек: '))
# number = 9 # данные для тестирования
family_dict = dict()
# family_dict = {'Alexei': 'Peter_I', 'Anna': 'Peter_I', 'Elizabeth': 'Peter_I', 'Peter_II': 'Alexei', 'Peter_III': 'Anna', 'Paul_I': 'Peter_III', 'Alexander_I': 'Paul_I', 'Nicholaus_I': 'Paul_I'}
family_range = dict()
count = 0

for i_num in range(1, number):
    print(i_num, 'пара: ', end='')
    pair = input('').split(' ')
    family_dict[pair[0]] = pair[1]

family_keys = set(family_dict.keys())
family_values = set(family_dict.values())
parent = family_values.difference(family_keys)
root = parent.pop()
family_range[root] = count

while len(family_range) != number:
    for i_member in family_dict:
        if i_member not in family_range and family_dict.get(i_member) in family_range:
            family_range[i_member] = family_range[family_dict.get(i_member)] + 1
    count += 1

print('\n"Высота" каждого члена семьи:')
for i_name in sorted(family_range):
    print(i_name, family_range[i_name])

# зачёт!
