number = int(input('Enter the number: '))
sum_numbers = 0
cur_numbers = 0

for i in range(1, number + 1):
    sum_numbers += i

for j in range(number - 1):
    cur = int(input('Enter current number: '))
    cur_numbers += cur

print('Missed_card =', sum_numbers - cur_numbers)


