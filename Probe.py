string = input('Enter the string: ')
summ = 0
summ_max = 0

for letter in string:
    if summ_max < summ:
        summ_max = summ
    if letter == 's':
        summ += 1
    else:
        summ = 0

print(summ_max)

