def func(line):
    try:
        if line.endswith('\n'):
            line = line[:-1]

        members = line.split(' ')
        first_operand = members[0]
        operation = members[1]
        second_operand = members[2]

        if not first_operand.isdigit():
            raise TypeError
        else:
            first_operand = int(first_operand)

        if not second_operand.isdigit():
            raise TypeError
        else:
            second_operand = int(second_operand)

        operation_list = '+-*/^'
        if len(operation) > 1:
            raise ArithmeticError
        elif operation not in operation_list:
            raise TypeError
        else:
            cmd = '{} {} {}'.format(first_operand, operation, second_operand)
            return eval(cmd)

    except (ArithmeticError, TypeError):
        print('Обнаружена ошибка в строке:', line)
        answer = input('Хотите исправить? ').lower()
        if answer == 'нет':
            return 0
        else:
            fixed_line = input('Введите исправленную строку: ')
            return func(fixed_line)


summ = 0

with open('calc.txt', 'r') as calc:
    for i_string in calc:
        result_of_string = func(i_string)
        summ += result_of_string

print('Сумма результатов:', summ)
