def summ(*data):
    result = 0
    for i_key, i_value in enumerate(data):
        if isinstance(i_value, int):
            result += i_value
        else:
            i_list = i_value
            for i_index in i_list:
                result += summ(i_index)
    return result


print('Вызов функции summ([[1, 2, [3]], [1], 3]):')
print('Ответ:', summ([[1, 2, [3]], [1], 3]))
print('Вызов функции summ(1, 2, 3, 4, 5):')
print('Ответ:', summ(1, 2, 3, 4, 5))
