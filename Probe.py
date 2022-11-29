secret_number = 7
count = 0

while True:
    count += 1
    number = int(input('Enter the number: '))
    if number > secret_number:
        print('Число больше, чем нужно. Попробуйте ещё раз!')
    elif number < secret_number:
        print('Число меньше, чем нужно. Попробуйте ещё раз!')
    else:
        print('Вы угадали! Число попыток:', count)
        break
