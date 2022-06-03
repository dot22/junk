def func(line):
    try:
        members = line.split(' ')
        first_operand = members[0]
        if not first_operand.isdigit():
            raise TypeError
        else:
            first_operand = int(first_operand)
        second_operand = members[2]
        if not second_operand.isdigit():
            raise TypeError
        else:
            second_operand = int(second_operand)
        op = members[1]
        op_list = '+-*/^'
        if len(op) > 1:
            raise ArithmeticError
        elif op not in op_list:
            raise ArithmeticError
        else:
            cmd = r'print({} {} {})'.format(first_operand, op, second_operand)


summ = 0

with open('calc.txt', 'r') as calc:
    for i_string in calc:
        if i_string.endswith('\n'):
            i_string = i_string[:-1]
        result_of_string = func(i_string)
        # summ += result_of_string

print('Сумма результатов:', summ)