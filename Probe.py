soldiers = int(input('How many soldiers: '))
rules = int(input('How many rules: '))
summ = 0
for soldier in range(soldiers - 4, 0, -4):
    ask = int(input('How many rules you know: '))
    if ask != rules:
        print('You must make', soldier * 10, 'pushups!')
        summ += soldier * 10
print('Total pushups:', summ)