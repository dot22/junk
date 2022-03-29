def sum(data, result=0):
    for i_count, i_value in enumerate(data):
        if isinstance(i_value, int):
            result += i_value
        else:
            sub_data = i_value
            sum(sub_data, result)
    return result


list_1 = [[1, 2, [3]], [4], 5]
list_2 = 1, 2, 3, 4, 5

sum(list_1)
sum(list_2)
print(sum(list_1))
# print(sum(list_2))
