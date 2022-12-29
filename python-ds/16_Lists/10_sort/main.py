number = int(input('Введите количество элементов списка: '))
list = []

for _ in range(number):
    list_item = int(input('Введите очередной элемент списка: '))
    list.append(list_item)

print('\nИзначальный список:', list)

for _ in range(number - 1):
    for order in range(number - 1):
        if list[order] > list[order + 1]:
            list[order], list[order + 1] = list[order + 1], list[order]

print('Отсортированный список:', list)

# зачёт!
