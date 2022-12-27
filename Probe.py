def operation(sign, members):
    string = ''
    if sign == '*' or sign == '/':
        result = 1
    elif sign == '+' or sign == '-':
        result = 0

    for i in range(members):
        next_member = int(input('Введите операнд: '))
        if sign == '+':
            result += next_member
        elif sign == '-':
            result -= next_member
        elif sign == '*':
            result *= next_member
        else:
            result /= next_member

        if i == 0:
            string = str(next_member)
        else:
            string = string + ' ' + sign + ' ' + str(next_member)

    print(string, '=', result)


action = input('Введите действие: ')
number = int(input('Сколько операндов? '))

operation(action, number)
