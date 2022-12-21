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
    result = degree(n) * degree2x(x, n) / factor2n(n)
    return result


def summ(x):
    test_result = row_member(x, 0)
    for i in range(1000):
        while row_member(x, i) > 0.2835:
            test_result += row_member(x, i)
            print('row member =', row_member(x, i))
            print(test_result)


precision = 0.001
x_dig = 5
summ(x_dig)
