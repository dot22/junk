import math


def sphere(radius):
    print('Площадь сферы:', 4 * math.pi * radius ** 2 )


def yellow(radius):
    print('Объем шара:', 4 / 3 * math.pi * radius ** 3)


r = float(input('Введите радиус планеты: '))
sphere(r)
yellow(r)
