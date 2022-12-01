number = int(input('Enter the number: '))
summ = 0

for i in range(number):
    summ += ((-1) ** i) / (2 ** i)
print(summ)
