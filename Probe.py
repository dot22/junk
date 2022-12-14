def gcd(first, second):
    while first != 0 and second != 0:
        if first > second:
            first, second = second, first % second
        else:
            second, first = first, second % first

    return first + second


first_number = int(input('Enter first number: '))
second_number = int(input('Enter second number: '))
result = gcd(first_number, second_number)
print('НОД =', result)
