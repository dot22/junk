num1 = int(input('N1: '))
num2 = int(input('N2: '))
num3 = int(input('N3: '))

if num1 == num2 == num3:
    print('3')
elif num1 == num2 or num1 == num3 or num2 == num3:
    print('2')
else:
    print(0)
