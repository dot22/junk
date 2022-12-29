def sum_numbers(N):
    summa = 0
    while N > 0:
        summa += N % 10
        N //= 10
    return summa


def count_numbers(N):
    counts = 0
    while N > 0:
        counts += 1
        N //= 10
    return counts


number = 500
summ = sum_numbers(number)
print('Сумма цифр:', summ)
count = count_numbers(number)
print('Количество цифр в числе:', count)
print('Разность суммы чисел и количества равна', summ - count)
