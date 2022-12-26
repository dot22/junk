print('Задача 10. Аннуитетный платёж')

# Кредит в сумме S млн руб.,
# выданный на n лет под i% годовых,
# подлежит погашению равными ежегодными выплатами в конце каждого года,
# включающими процентные платежи и сумму в погашение основного долга.
#
# Проценты начисляются в один раз в год.
# После выплаты третьего платежа
# достигнута договорённость между кредитором и заёмщиком
# о продлении срока погашения займа на n_2 лет
# и увеличении процентной ставки с момента конверсии до i_2%.
#
# Напишите программу,
# которая выводит план погашения оставшейся части долга.
#
# A = KS
#
# K = i(1 + i) ** n / (1 + i) ** n - 1
#
# Пример:
#
# Введите сумму кредита: 40e6
# На сколько лет выдан? 5
# Сколько процентов годовых? 6
#
# Период: 1
#
# Остаток долга на начало периода: 40000000.0
# Выплачено процентов: 2400000.0
# Выплачено тела кредита: 7095856.02
#
#
# Период: 2
#
# Остаток долга на начало периода: 32904143.98
# Выплачено процентов: 1974248.6387999998
# Выплачено тела кредита: 7521607.3812
#
# Период: 3
#
# Остаток долга на начало периода: 25382536.5988
# Выплачено процентов: 1522952.195928
# Выплачено тела кредита: 7972903.824072
#
# Остаток долга: 17409632.774728
#
# =================================================
#
# На сколько лет продляется договор? 2
# Увеличение ставки до: 10
#
# Период: 1
#
# Остаток долга на начало периода: 17409632.774728
# Выплачено процентов: 1740963.2774728
# Выплачено тела кредита: 3751267.5625271997
#
# Период: 2
#
# Остаток долга на начало периода: 13658365.2122008
# Выплачено процентов: 1365836.52122008
# Выплачено тела кредита: 4126394.3187799198
#
# Период: 3
#
# Остаток долга на начало периода: 9531970.89342088
# Выплачено процентов: 953197.0893420881
# Выплачено тела кредита: 4539033.750657911
#
# Период: 4
#
# Остаток долга на начало периода: 4992937.142762969
# Выплачено процентов: 499293.71427629696
# Выплачено тела кредита: 4992937.125723703
#
# Остаток долга: 0.017039266414940357

'''
# annuity_payment = coefficient * amount_credit
# 
# coefficient = loan_percentage * (1 + loan_percentage) ** credit_term / ((1 + loan_percentage) ** credit_term - 1)

# amount_credit - сумма кредита
# loan_percentage - процент по кредиту
# credit_term - срок кредита

'''


def calc_coefficient(loan_percentage, credit_term):
    coefficient = loan_percentage * (1 + loan_percentage) ** credit_term / ((1 + loan_percentage) ** credit_term - 1)
    return coefficient


def calc_annuity_payment(coefficient, amount_credit):
    annuity_payment = round(coefficient * amount_credit, 2)
    return annuity_payment


#amount_credit = 40e6
amount_credit = float(input('Введите сумму кредита: '))

#credit_term = 5
credit_term = int(input('На сколько лет выдан? '))

#loan_percentage = 6 / 100
loan_percentage = float(input('Сколько процентов годовых? ')) / 100

coefficient = calc_coefficient(loan_percentage, credit_term)
annuity_payment = calc_annuity_payment(coefficient, amount_credit)

for year in range(1,credit_term - 1):
    print('\nПериод', year)
    print('Остаток долга на начало периода:', round(amount_credit, 2))
    print('Выплачено процентов:', round(amount_credit * loan_percentage, 2))
    print('Выплачено тела кредита:', round((annuity_payment - amount_credit * loan_percentage), 2))
    amount_credit -= annuity_payment - amount_credit * loan_percentage
    credit_term -= 1

print('\n\nОстаток долга:', round(amount_credit, 2))
print('Осталось платить лет:', credit_term)

print('\n==========\n')

#credit_term += 2
credit_term += int(input('На сколько лет продлевается договор? '))

#loan_percentage = 0.1
loan_percentage = float(input('Увеличение ставки до: ')) / 100

coefficient = calc_coefficient(loan_percentage, credit_term)
annuity_payment = calc_annuity_payment(coefficient, amount_credit)

for year in range(1,credit_term + 1):
    print('\nПериод', year)
    print('Остаток долга на начало периода:', round(amount_credit, 2))
    print('Выплачено процентов:', round(amount_credit * loan_percentage, 2))
    print('Выплачено тела кредита:', round((annuity_payment - amount_credit * loan_percentage), 2))
    amount_credit -= annuity_payment - amount_credit * loan_percentage
    credit_term -= 1

print('\n\nОстаток долга (округленно):', round(amount_credit, 2))
print('Остаток долга:', amount_credit)
#print('Осталось платить лет:', credit_term)
