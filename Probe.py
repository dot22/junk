def reverse_number(num):
    reverse = 0
    degree = 0
    while num > 0:
        reverse = reverse * 10 + num % 10
        num //= 10
        degree += 1
    print(reverse)


while True:
    number = int(input('Enter the number: '))
    if number != 0:
        reverse_number(number)
    else:
        print('Program is closed')
        break
