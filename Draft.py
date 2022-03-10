def range_num(num):
    if num == 0:
        return 0
    range_num(num - 1)
    print(num)


number = int(input('Введите число: '))
print('Вывод всех чисел от 1 до', number)
range_num(number)
