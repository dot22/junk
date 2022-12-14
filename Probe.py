number = float(input('Enter the number: '))

order = 0

if number < 0:
    print('Wrong number')
elif number < 1:
    while number < 1:
        order -= 1
        number = number * 10
elif number >= 10:
    while number >= 10:
        number /= 10
        order += 1

print(round(number, abs(order)), order)
