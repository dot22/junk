number = int(input('Введите число N: '))
number_list = []

for order in range(1, number + 1, 2):
    number_list.append(order)

print('Список из нечётных чисел от одного до N:', number_list)

# зачёт!
