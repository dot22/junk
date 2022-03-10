def range_num(num):
    if num == 0:
        return 0
    print(initial_num - num)
    return range_num(num - 1)




number = int(input('Введите число: '))
print('Вывод всех чисел от 1 до', number)
range_num(number)
