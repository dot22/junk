size = 5

for row in range(1, size + 1):
    for col in range(1, size + 1):
        if row % 2 == 0:
            print(row, end=' ')
        else:
            print(col, end=' ')
    print()

