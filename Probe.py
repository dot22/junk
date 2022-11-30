number = int(input('Enter the number: '))

for i in range(1, number // 2 + 1):
    print(i * 2, '** 3 =', (i * 2) ** 3)