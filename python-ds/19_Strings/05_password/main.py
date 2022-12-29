while True:
    password = input('Придумайте пароль: ')
    if len(password) < 8:
        print('Пароль ненадёжный.\nВ пароле должно быть не менее 8 символов.\nПопробуйте ещё раз.')
    elif len([i_sym for i_sym in password if i_sym.isupper()]) < 1:
        print('Пароль ненадёжный.\nВ пароле должна быть хотя бы одна большая буква.\nПопробуйте ещё раз.')
    elif len([i_sym for i_sym in password if i_sym.isdigit()]) < 3:
        print('Пароль ненадёжный.\nВ пароле должно быть не менее трех цифр.\nПопробуйте ещё раз.')
    else:
        print('\nЭто надёжный пароль!')
        break

# зачёт!
