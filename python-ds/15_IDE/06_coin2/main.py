from math import sqrt


def hypotenuse(x, y):
    return sqrt(x ** 2 + y ** 2)


print('Введите координаты монетки:')
coordinate_X = float(input('X: '))
coordinate_Y = float(input('Y: '))
radius = float(input('Введите радиус: '))

if radius >= hypotenuse(coordinate_X, coordinate_Y):
    print('\nМонетка где-то рядом:')
else:
    print('\nМонетки в области нет')

# зачёт!
