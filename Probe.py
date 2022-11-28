# bank_account = int(input('Bank account: '))
bank_account = 10
# percent = int(input('Percent: '))
percent = 10
# max_amount = int(input('Max amount: '))
max_amount = 50
years = 0

while bank_account < max_amount:
    years += 1
    bank_account = (bank_account + bank_account * percent / 100) * 10000 // 100 / 100
    print(bank_account)

print(years)
