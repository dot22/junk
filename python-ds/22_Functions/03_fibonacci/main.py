def fibonachi_pos(num):
    if num <= 1:
        return num
    return fibonachi_pos(num - 1) + fibonachi_pos(num - 2)


num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))

print(fibonachi_pos(num_pos))
