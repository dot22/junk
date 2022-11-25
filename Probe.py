amount = int(input('How much do you have: '))

while amount < 10000:
    dice = int(input('Enter the dice: '))
    if dice == 3:
        print('You are loose all')
        amount = 0
        break
    print('You up 500')
    amount += 500
print(amount)