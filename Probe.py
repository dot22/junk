def nod(num1, num2):
    while (num1 != 0) and (num2 != 0):
        if num1 > num2:
            num1, num2 = num2, num1 % num2
            nd = num1
        else:
            num2, num1 = num1, num2 % num1
            nd = num2
    print('NOD =', nd)


number1 = int(input('Number 1: '))
number2 = int(input('Number 2: '))
nod(number1, number2)
