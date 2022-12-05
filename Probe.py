amount_numbers = int(input('Enter numbers: '))
max_number = 0
max_summ = 0

for order in range(amount_numbers):
    number = int(input('Enter the number: '))
    number_summ = 0
    test_number = number
    while test_number > 0:
        number_summ += test_number % 10
        test_number //= 10
    if number_summ > max_summ:
        max_summ = number_summ
        max_number = number

print(max_number, max_summ)