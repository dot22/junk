first = int(input('Первый товар: '))
second = int(input('Второй товар: '))
third = int(input('Третий товар: '))
summ = first + second + third
if summ > 10000:
    summ -= summ * 10 / 100
print('Итоговая сумма =', summ)
