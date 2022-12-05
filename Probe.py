number = int(input('Enter the number: '))
summ = 0

for i in range(1, number + 1):
    for j in range(1, i):
        i *= j
    summ += i

print(summ)
