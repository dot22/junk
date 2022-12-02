x = int(input('X: '))
res = 1
for i in range(1, 65):
    if i % 2 != 0:
        res *= (x - i)
    else:
        res /= (x - i)
print(res)