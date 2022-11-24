a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

maxn = a

if maxn < b:
    maxn = b

if maxn < c:
    maxn = c

print(maxn)
