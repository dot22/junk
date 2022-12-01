start = int(input('Start: '))
finish = int(input('Finish: '))
step = int(input('Step: '))

for x in range(finish, start -1, step):
    y = x ** 3 + 2 * x ** 2 - 4 * x + 1
    print(y)
