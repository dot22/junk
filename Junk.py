names_file = open('names.txt', 'r')
sym_sum = 0

try:
    for i_line in names_file:
        length = len(i_line)
        if i_line.endswith('\n'):
            length -= 1
        if length < 3:
            raise BaseException('Длина строки меньше трех символов')
        sym_sum += length
finally:
    print('Общее количество символов: ', sym_sum)

