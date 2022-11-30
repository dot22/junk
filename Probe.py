total_hours = int(input('Enter total hours: '))
cell = 1

for hour in range(1, total_hours // 3 + 1):
    cell *= 2
    print('Прошло:', hour * 3, 'hours')
    print('Клеток:', cell)
    print('До конца эксперимента:', total_hours - hour * 3)
