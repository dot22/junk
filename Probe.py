work_time = int(input('Введите отработанные часы: '))
credit = int(input('Введите остаток по кредиту: '))
food = int(input('Введите траты на еду: '))

sellary = (200 * work_time) / (2 ** 3) + work_time

if sellary >= credit + food:
    print('Часов хватает. Можете отдохнуть')
else:
    print('Часов не хватает. Придется работать')