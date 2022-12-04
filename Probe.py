size = int(input('Enter the size: '))

for row in range(size):
    for col in range(size):
        if col == size - row - 1:
            print('1', end='')
        elif col < size - row - 1:
            print('0', end='')
        else:
            print('2', end='')
    print()
