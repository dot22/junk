def search(x, y, r):
    if x ** 2 + y ** 2 <= r ** 2:
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')
    return


x1 = 0.5
y1 = 0.5
r1 = 1
search(x1, y1, r1)

x2 = 2
y2 = 2
r2 = 2
search(x2, y2, r2)
