def min_num(num1, num2):
    summ = num1 + num2
    diff = abs(num1 - num2)
    min = (summ - diff) / 2
    print(min)


num1 = int(input('Number 1: '))
num2 = int(input('Nuber 2: '))
min_num(num1, num2)
