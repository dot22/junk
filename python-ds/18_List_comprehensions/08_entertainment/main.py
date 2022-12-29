def game_list_fill(order):
    print('Бросок ', order, '. Сбиты палки с номера ', sep='', end='')
    L_i = int(input())
    R_i = int(input('по номер '))
    return [L_i - 1, R_i - 1]


sticks = int(input('Количество палок: '))
casts = int(input('Количество бросков: '))

game_list = []  # строка кода получилась лишней, т.к. переменная создаётся в коде ниже.
result = ''

field_list = ['|' for _ in range(sticks)]

game_list = [game_list_fill(i_order) for i_order in range(1, casts + 1)]

for i_game in game_list:
    for i_shoot in range(i_game[0], i_game[1] + 1):
        field_list[i_shoot] = '.'

for i_place in field_list:
    result += i_place

print('Результат:', result)

# зачёт!
