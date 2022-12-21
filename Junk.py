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

i = 0
x_dig = 5
precision = 0.001

while True:
    test_result = row_member(x_dig, i)
    if abs(test_result + row_member(x_dig, i + 1) - test_result) > precision:
        print()
        print('i =', i)
        # degree(i)
        # degree2x(5, i)
        # factor2n(i)
        test_result += row_member(x_dig, i + 1)
        i += 1
        print(test_result)
        print()
    else:
        print(test_result)
        break

