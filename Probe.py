def rate(i, n):
    k = i * ((1 + i) ** n) / ((1 + i) ** n - 1)
    return k


def annuity(k, s):
    a = k * s
    return a


credit = 40e6
years = 5
percent = 0.06

every_month = round(annuity(rate(percent, years), credit), 2)

for year in range(3):
    print('Период:', year + 1)
    print('Остаток долга на начало периода:', credit)
    this_year_percent = credit * percent
    print('Выплачено процентов:', this_year_percent)
    body_credit = every_month - this_year_percent
    print('Выплачено тела кредита:', body_credit)
    credit -= body_credit
    print()

print('Остаток долга:', credit, '\n\n==========\n')

years = 4
percent = 0.10
every_month = round(annuity(rate(percent, years), credit), 2)

for year in range(years):
    print('Период:', year + 1)
    print('Остаток долга на начало периода:', credit)
    this_year_percent = credit * percent
    print('Выплачено процентов:', this_year_percent)
    body_credit = every_month - this_year_percent
    print('Выплачено тела кредита:', body_credit)
    credit -= body_credit
    print()

print('Остаток долга:', credit, '\n\n==========\n')
