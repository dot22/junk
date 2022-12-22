def degree(n):
    result = 1
    for j in range(n):
        result *= -1
    # print('degree =', result)
    return result


def degree2x(x, n):
    result = 1
    for j in range(2 * n):
        result *= x
    # print('degree2x =', result)
    return result


def factor2n(n):
    result = 1
    for i in range(1, 2 * n + 1):
        result *= i
    # print('factor2n =', result)
    return result


def row_member(x, n):
    result = degree(n) * degree2x(x, n) / factor2n(n)
    # print('result =', result)
    return result


x_dig = 5
precision = 0.001

summ = 0
i = 0
while True:
    print('\ni =', i)
    print('row member =', row_member(x_dig, i))
    print('next member =', row_member(x_dig, i + 1))
    if abs(row_member(x_dig, i) + abs(row_member(x_dig, i + 1) - abs(row_member(x_dig, i)))) > precision:
        summ += row_member(x_dig, i)
        print('summ =', summ)
        i += 1
    else:
        break
