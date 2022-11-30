number = int(input('Enter the Number: '))

for i in range(1, number // 2 + 2):
    print((i * 2) - 1, '** 2 =', ((i * 2) - 1) ** 2)
