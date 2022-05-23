numbers_file = open('numbers.txt', 'r')
answer_file = open('answer.txt', 'w')
summ = 0

try:
    for i_line in numbers_file:
        i_line = i_line.split()
        for i_sym in i_line:
            if i_sym.isdigit():
                summ += int(i_sym)

    answer_file.write(str(summ))
finally:
    numbers_file.close()
    print('number_file закрыт корректно')
    answer_file.close()
    print('answer_file закрыт корректно')
