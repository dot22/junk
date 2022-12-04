number = int(input('Enter the number: '))

for row in range(number + 1):
    for col in range(row, number + 1):
        if row <= col:
            print(col, end=' ')
    print()
