number = int(input('Enter the number: '))
summ = 0
for i in range(1, number + 1, 5):
    print('Номер стула:', i)
    summ += i
print(summ)