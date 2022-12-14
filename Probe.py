def eqv(a, b, c):
    if a + b - c > 1e-16:
        print('True')
    else:
        print('False')
    print(a + b, c)

eqv(1.1, 2.2, 3.3)
eqv(1e-14, 1e-14, 3e-14)