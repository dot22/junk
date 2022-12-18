def degree(number):
    result = 1
    for j in range(number):
        result *= -1
    return result


for i in range(3):
    print('i =', i)
    print(degree(i))
