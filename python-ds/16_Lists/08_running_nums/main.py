number = int(input('Введите количество элементов списка: '))
running_list = []

for _ in range(number):
    list_item = int(input('Введите очередной элемент списка: '))
    running_list.append(list_item)

shift = int(input('\nСдвиг: '))
print('Изначальный список:', running_list)

for _ in range(shift):
    temp_value = running_list[-1]
    for order in range(len(running_list) - 1, -1, -1):
        running_list[order] = running_list[order - 1]
    running_list[0] = temp_value

print('Сдвинутый список:', running_list)

# зачёт!
