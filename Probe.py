num1 = int(input('Enter number one: '))
num2 = int(input('Enter number two: '))
num3 = int(input('Enter number three: '))

if num1 > num2 and num1 > num3:
    print('max -', num1)
elif num2 > num1 and num2 > num3:
    print('max -', num2)
else:
    print('max -', num3)