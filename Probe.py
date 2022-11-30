numbers = 3, 5, 4, 3, 3, 4, 5, 3, 3, 4, 4, 3, 4
n3 = 0
n4 = 0
n5 = 0

for i in numbers:
    if i == 3:
        n3 += 1
    elif i == 4:
        n4 += 1
    else:
        n5 += 1

if n3 > n4 and n3 > n5:
    print('n3')
elif n4 > n3 and n4 > n5:
    print('n4')
else:
    print('n5')