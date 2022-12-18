# def degree(number):
#     result = 1
#     for j in range(number):
#         result *= -1
#     return result


# def degree2x(number, x):
#     result = 1
#     for j in range(2 * number):
#         result *= x
#     return result

def factor2n(number):
    result = 1
    for j in range(1, number * 2 + 1):
        result *= j
    return result


for i in range(3):
    print(factor2n(i))
