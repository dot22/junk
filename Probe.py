first_list = [1, 2, 3]
print('Первый список:', first_list)
second_list = [2, 4, 6, 3, 3, 2, 1]
print('Второй список', second_list)

first_list.extend(second_list)
print('Расширенный первый список:', first_list)

for i in first_list:
    for j in range(first_list.count(i) - 1):
        first_list.remove(i)

print(first_list)
