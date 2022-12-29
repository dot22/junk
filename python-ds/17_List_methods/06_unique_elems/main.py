list_1 = []
list_2 = []

for i_num in range(1, 4):
    print('Введите', i_num, 'число первого списка:', end=' ')
    number = int(input())
    list_1.append(number)

for i_num in range(1, 8):
    print('Введите', i_num, 'число второго списка:', end=' ')
    number = int(input())
    list_2.append(number)

print('\nПервый список:', list_1)
print('Второй список:', list_2)

list_1.extend(list_2)

for i_elem in list_1:
    for _ in range(list_1.count(i_elem) - 1):
        list_1.remove(i_elem)

print('\nНовый первый список с уникальными элементами:', list_1)

# зачёт!