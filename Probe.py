size = int(input('Enter the size: '))
count = 1

for row in range(1, size + 1):
    print((size - row) * '_', end='')
    for col in range(row):
        print(count, end=' ')
        count += 2
    print()
