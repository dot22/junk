creditors = int(input('How many creditors: '))
summ = 0

for i in range(0, creditors, 5):
    print('Creditor number', i)
    credit = int(input('How much do you loan: '))
    summ += credit

print(summ)
