count_positive = 0
count_negative = 0
while True:
    number = int(input('Enter the number: '))
    if number > 0:
        count_positive += 1
    elif number < 0:
        count_negative += 1
    else:
        break

print('Positive -', count_positive)
print('Negative -', count_negative)
