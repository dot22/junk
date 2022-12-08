import math


sequence = int(input('Enter sequence: '))

for i in range(sequence):
    x = float(input('Enter X: '))
    if x > 0:
        x = math.ceil(x)
        print('x = ', x, ', log(x) =', math.log(x))
    else:
        x = math.floor(x)
        print('x =', x, ', exp(x) =', math.exp(x))