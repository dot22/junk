def validation(data, number):
    personal_data = data.split()
    try:
        if len(personal_data) != 3:
            raise IndexError
        if not personal_data[0].isalpha():
            raise NameError
        if ('@' or '.') not in personal_data[1]:
            raise SyntaxError
        # if not personal_data[2].isdigit() or not (10 <= int(personal_data[2]) <= 99):
        if not (10 <= int(personal_data[2]) <= 99):
            raise ValueError
    except IndexError:
        bad_log.write('Строка ' + str(number) + ':' + str(personal_data) + ' - НЕ присутствуют все три поля\n')
    except NameError:
        bad_log.write('Строка ' + str(number) + ':' + str(personal_data) + ' - поле имени содержит НЕ только буквы\n')
    except SyntaxError:
        bad_log.write('Строка ' + str(number) + ':' + str(personal_data) + ' - поле емейл НЕ содержит @ и . (точку)\n')
    except ValueError:
        bad_log.write('Строка ' + str(number) + ':' + str(personal_data) + ' - поле возраст НЕ является числом от 10 до 99\n')
    else:
        good_log.write(' '.join(personal_data) + '\n')


line_number = 0

with open('registrations.txt', 'r') as registration, \
        open('registrations_bad.log', 'w') as bad_log, \
        open('registrations_good.log', 'w') as good_log:
    for user_data in registration:
        line_number += 1
        validation(user_data, line_number)
