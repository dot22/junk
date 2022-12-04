number = int(input('Enter the number: '))

for row in range(1, number + 1):
    for col in range(1, number + 1):
        if row >= col:
            print(row, end='')
    print()
