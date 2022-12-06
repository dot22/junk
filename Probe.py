# size = int(input('Enter size: '))
size = 6

for row in range(size):
    for col in range(size * 2):
        if col <= row:
            print(size - col, end='')
        elif col >= size * 2 - row - 1:
            print(col - size + 1, end='')
        else:
            print(' ', end='')
    print()
