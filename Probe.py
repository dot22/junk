a = int(input('A: '))
b = int(input('B: '))
summ = 0
count = 0

for i in range(a, b + 1):
    if i % 3 == 0:
        count += 1
        summ += i

print('Answer:', summ / count)