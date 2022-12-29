def reverse_number(number):
    part = ''
    first_part = ''
    # Если переменную цикла используем в коде, её необходимо назвать так, чтобы название отражало суть содержания.
    #  "_" не отражает.
    for _ in number:
        if _ != '.':
            part = _ + part
        else:
            first_part = part
            part = ''
    number = first_part + '.' + part
    return float(number)


number_1 = input('Введите первое число: ')
number_2 = input('Введите второе число: ')

reverse_number_dig_1 = reverse_number(number_1)
reverse_number_dig_2 = reverse_number(number_2)

print('\nПервое число наоборот:', reverse_number_dig_1)
print('Второе число наоборот:', reverse_number_dig_2)
print('Сумма:', reverse_number_dig_1 + reverse_number_dig_2)

'''
# , предлагаю попробовать сократить количество вызовов наших функций.
#  т.к. каждый вызов функции это отдельное действие для python, которое создаёт нагрузку на код.
#  Возможно мы сможем создать переменные с возвратом функций и использовать в работе их?
'''

# зачёт!
