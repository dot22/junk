def summ(data):
    result = 0
    for i_value in data:
        if isinstance(i_value, int):
            i_summ = i_value
        else:
            i_summ = summ(i_value)
        result += i_summ
    return result


list_1 = [[1, 2, [3]], [1], 3]
list_2 = 1, 2, 3, 4, 5
print(list_1)
print('Ответ:', summ(list_1))
print(list_2)
print('Ответ:', summ(list_2))
