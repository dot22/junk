number = 50
number_min = 0
number_max = 100
count = 0

while True:
    count += 1
    print('Попытка номер', count)
    print('Твоё число равно, меньше или больше, чем число ', number, '?', sep='')
    answer = int(input('1 — равно, 2 — больше, 3 — меньше: '))
    if answer == 1:
        print('Your number is', number)
        print('Game is over!')
        break
    elif answer == 2:
        number_min = number
        number = (number_max + number_min) // 2
    else:
        number_max = number
        number = (number_max + number_min) // 2
