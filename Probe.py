import math


def distance(x, y):
    print('Дистанция:', math.sqrt(x ** 2 + y ** 2))


def lenght(x1, x2, y1, y2):
    print('Длина отрезка:', math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))


choise = int(input('Что выбрать 1 или 2'))
if choise == 1:
    x = int(input('X: '))
    y = int(input('Y: '))
    distance(x, y)
elif choise == 2:
    x1 = int(input('X1: '))
    y1 = int(input('Y1: '))
    x2 = int(input('X2: '))
    y2 = int(input('Y2: '))
    lenght(x1, x2, y1, y2)
else:
    print('Wrong number')
