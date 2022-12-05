size = 11

for row in range(size):
    for col in range(size + 1):
        if row == col:
            print('^', end='')
        elif row == size - col:
            print('^', end='')
        else:
            print(' ', end='')
    print()
