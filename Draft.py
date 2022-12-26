def degree(n):
    result = 1
    for j in range(n):
        result *= -1
    return result


def degree2x(x, n):
    result = 1
    for j in range(2 * n):
        result *= x
    return result


def factor2n(n):
    result = 1
    for i in range(1, 2 * n + 1):
        result *= i
    return result


x = 5
precursion = 0.0001
summ = 0
i = 0

while True:
    cur_member = degree(i) * degree2x(x, i) / factor2n(i)
    next_member = degree(i + 1) * degree2x(x, i + 1) / factor2n(i + 1)
    if abs(cur_member + next_member - cur_member) >= precursion:
        summ += cur_member
        print(summ)
        i += 1
        print('i =', i, '\n')
    else:
        print('summ =', summ)
        break


# for i in range(5):
#     print('i =', i)
#     degree(i)
#     degree2x(5, i)
#     factor2n(i)
#     print('member =', degree(i) * degree2x(5, i) / factor2n(i))
#     print()
