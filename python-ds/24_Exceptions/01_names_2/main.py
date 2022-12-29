# -*- coding: utf-8 -*-

def check_lenght(word, line):
    with open('errors.log', 'a') as errors_log:
        try:
            length = len(word)
            if word.endswith('\n'):
                length -= 1
            if length < 3:
                raise ValueError
        except ValueError:
            print('Ошибка: в строке {} меньше трех символов'.format(line))
            errors_log.write('В строке {} меньше трех символов\n'.format(line))
        finally:
            return length


sym_sum = 0
line_count = 0

with open('people.txt', 'r', encoding='utf-8') as peoples_file:
    for i_line in peoples_file:
        line_count += 1
        sym_count = check_lenght(i_line, line_count)
        # if sym_count:
        sym_sum += sym_count

print('Общее количество символов:', sym_sum)
