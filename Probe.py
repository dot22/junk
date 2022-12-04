seq_numbers = int(input('How many numbers: '))
amount = 0

for order in range(seq_numbers):
    number = input('Enter next number: ')
    for numeral in number:
        # print(numeral)
        if int(numeral) > 5:
            amount += 1

print('Amount numerals:', amount)
