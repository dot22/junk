x = int(input('Enter X size: '))
y = int(input('Enter Y size: '))

for row in range(y):
    for col in range(x):
        if col == 0 or col == x - 1:
            print('|', end='')
        elif row == 0 or row == y - 1:
            print('-', end='')
        else:
            print(' ', end='')
    print()
