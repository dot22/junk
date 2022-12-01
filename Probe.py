scholarship = int(input('Enter the scholarship: '))
expenses = int(input('Enter the expenses: '))
full_expenses = 0

for month in range(10):
    if month != 0:
        expenses = expenses + expenses * 3 / 100
    full_expenses += expenses

full_scholarship = scholarship * 10

summ = full_expenses - full_scholarship
print(summ)

