def summ(*data):
    result = 0
    for i_value in data:
        if isinstance(i_value, int):
            i_summ = i_value
        else:
            i_summ = summ(i_value)
        result += i_summ
    return result


print('summ([[1, 2, [3]], [1], 3])')
print('Ответ:', summ([[1, 2, [3]], [1], 3]))

print('summ(1, 2, 3, 4, 5)')
print('Ответ:', summ(1, 2, 3, 4, 5))
