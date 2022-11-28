number = int(input('Enter the number: '))

number1 = number // 1000
number2 = number % 1000
sum1 = number1 % 10 + number1 // 10 % 10 + number1 // 100
sum2 = number2 % 10 + number2 // 10 % 10 + number2 // 100
if sum1 == sum2:
    print('Good Luck!')
else:
    print('You loose')