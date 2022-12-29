list_main = [1, 5, 3]
list_1 = [1, 5, 1, 5]
list_2 = [1, 3, 1, 5, 3, 3]

list_main.extend(list_1)

print('Количество цифр 5 при первом объединении:', list_main.count(5))

while 5 in list_main:
    list_main.remove(5)

list_main.extend(list_2)

print('Количество цифр 3 при первом объединении:', list_main.count(3))
print('Итоговый список:', list_main)

# зачёт!
