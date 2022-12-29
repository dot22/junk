number = int(input('Количество клеток: '))
cell_list = []

for rang in range(number):
    print('Эффективность', rang + 1, 'клетки:', end=' ')
    efficiency = input()
    if int(efficiency) < rang:
        cell_list.append(efficiency)

string_list = ' '.join(cell_list)
print('Неподходящие значения:', string_list)

# зачёт!
