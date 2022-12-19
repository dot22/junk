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


# def row_member(x, n):
#     result = 1
#     result *= degree(n) * degree2x(x, n) / factor2n(n)
#     return result

def summ(x):
    n = 0
    current_row_member = degree(n) * degree2x(x, n) / factor2n(n)
    next_row_member = degree(n + 1) * degree2x(x, n + 1) / factor2n(n + 1)
    while abs(current_row_member + next_row_member) - abs(next_row_member) > 0.001:
        current_row_member += next_row_member
        next_row_member = degree(n + 1) * degree2x(x, n + 1) / factor2n(n + 1)
        n += 1
    print(current_row_member)


precision = 0.001
x_dig = 5
summ(x_dig)
