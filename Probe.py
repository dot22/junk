x_start = 1
x_end = 15
x = 8
y_start = 1
y_end = 20
y = 10

while True:
    print('Марсоход находится на позиции ', x, ', ', y, ', введите команду:', sep='')
    command = input('Команда: ')
    if command == 'a' or command == 'A':
        if x - 1 >= x_start:
            x -= 1
    if command == 'd' or command == 'D':
        if x + 1 <= x_end:
            x += 1
    if command == 'w' or command == 'W':
        if y + 1 <= y_end:
            y += 1
    if command == 's' or command == 'S':
        if y - 1 >= y_start:
            y -= 1
    if command == '0':
        break

