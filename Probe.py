text = input('Enter the text: ')
count_big = 0
count_small = 0

for i in text:
    if i == 'Ы':
        count_big += 1
    elif i == 'ы':
        count_small += 1

print('Big:', count_big)
print('Small:', count_small)