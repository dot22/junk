a = int(input('Enter the size: '))
count = 0
envelop = 12 * 12

while a ** 2 > envelop:
    count += 1
    a = a / 2

print(count)
