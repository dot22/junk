level1 = 1000
level2 = 2500
level3 = 5000

count = int(input('Введите количество опыта: '))

if count > level3:
    print('Ваш уровень: 3')
elif count > level2:
    print('Ваш уровень:', 2)
elif count > level1:
    print('Ваш уровень: 1')
elif count < level1:
    print('Ваш уровень: 0')