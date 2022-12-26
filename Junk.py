def sign(order):
    sign = 1
    for i in range(order):
        sign *= -1
    return sign


def degree(number, order):
    degree = 1
    for i in range(order * 2):
        degree *= number
    return degree


def factorial(order):
    if order == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, 2 * order + 1):
            factorial *= i
        return factorial


def summing(number, order):
    summing = sign(order) * degree(number, order) / factorial(order)
    return summing


number = float(input('Введите x: '))
precision = float(input('Введите точность: '))

summ = 0
order = 0

while abs(summing(number, order)) > precision:
    summ += summing(number, order)
    order += 1

print('Сумма ряда =', summ)
