def degree(n):
    result = 1
    for j in range(n):
        result *= -1
    print('degree =', result)
    return result


def degree2x(x, n):
    result = 1
    for j in range(2 * n):
        result *= x
    print('degree2x =', result)
    return result


def factor2n(n):
    result = 1
    for i in range(1, 2 * n + 1):
        result *= i
    print('factor2n =', result)
    return result


def row_member(x, n):
    result = 1
    result *= degree(n) * degree2x(x, n) / factor2n(n)
    return result


def summ(x):
    n = 0
    present_row_member = row_member(x, n)
    next_row_member = row_member(x, n + 1)
    while abs(present_row_member) - abs(next_row_member) > precision:
        present_row_member += next_row_member
        next_row_member = row_member(x, )
        n += 1

    print(row_member(x, n))


precision = 0.001
x_dig = 5
summ(x_dig)
