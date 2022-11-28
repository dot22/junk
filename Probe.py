name = input('Name: ')
credit = int(input('Credit: '))

print(name, 'your credit is', credit, 'roubles.')

while True:
    ask = int(input('How much can you pay? '))
    if ask >= credit:
        break
    else:
        print('Маловато, Василий. Давайте ещё раз.')
print('Отлично,', name, '! Вы погасили долг. Спасибо!')
