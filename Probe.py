a = int(input('A: '))
b = int(input('B: '))

c = a + b
d = a - b

min = (c - abs(d)) / 2
max = min + abs(d)

print(min, max)

