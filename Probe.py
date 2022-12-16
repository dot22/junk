def count_digits(number):
    count = 1
    while number // 10 > 0:
        count += 1
        number //= 10
    return count


def changed_number(number, restrict):
    if count_digits(number) < restrict:
        print('Не хватает цифр')
        return
    else:
        return between_digits(number)


def between_digits(number):
    count = len(str(number))
    first = number // (10 ** (count - 1))
    last = number % 10
    result = (number - (first * 10 ** (count - 1)) - last + last * 10 ** (count - 1) + first)
    print(result)
    return result


def sum_numbers(a, b):
    c = int(a) + int(b)
    return c


c = count_digits(123)
d = count_digits(4567)
e = changed_number(123, 3)
f = changed_number(4567, 4)
g = sum_numbers(e, f)
print(g)
