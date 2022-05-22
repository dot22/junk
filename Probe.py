import os


try:
    ages = open('ages.txt', 'r')
    result = open('result.txt', 'x')
    for i_line in ages:
        age_round = round(i_line, 2)
        result.write(age_round)
except FileExistsError:
    print('Файл с таким именем уже существует')
except IsADirectoryError:
    print('Под указанным имненем существует каталог, но не файл')
except TypeError:
    print('Некорректный тип данных или некорретное значение')
