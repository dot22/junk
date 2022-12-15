def max_two(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


a = int(input('Enter A: '))
b = int(input('Enter B: '))
c = int(input('Enter C: '))

d = max_two(a, b)
print(max_two(c, d))
