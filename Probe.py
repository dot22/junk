import math

a = float(input('A: '))
b = float(input('B: '))
c = float(input('C: '))

d = (b ** 2) - (4 * a * c)

print('D =', d)

if d < 0:
    print('No way')
elif d == 0:
    x = (-1 * b) / (2 * a)
    print('X =', x)
else:
    x1 = (-1 * b + math.sqrt(d)) / (2 * a)
    x2 = (-1 * b - math.sqrt(d)) / (2 * a)
    if x1 < x2:
        print(x1, x2)
    else:
        print(x2, x1)
