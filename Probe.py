count = 0

for i in range(30, 36):
    print('Людей в секторе', i, end='')
    puple = int(input(': '))
    if puple <= 10:
        print('Всё спокойно')
    else:
        print('Нарушение!')
        count += 1
print('Нарушений -', count)