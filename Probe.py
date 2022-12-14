budget = float(input('Enter the budget: '))
tax = float(input('Enter the tax: '))

if (budget + tax) - budget < 1e-16:
    print('Budget grows')
else:
    print('The same')
print(budget, tax)
print(budget)
