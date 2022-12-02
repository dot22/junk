count = 0
for i in range(5):
    ask = input('Кто написал Онегина? ')
    if ask == 'Пушкин' or ask == 'пушкин':
        break
    print('Wrong answer.')
    count += 1

print('Bad boys:', count)