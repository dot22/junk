def number_sum(number_init):
    sum_number = 0
    # Если переменную цикла используем в коде, её необходимо назвать так, чтобы название отражало суть содержания.
    #  "_" не отражает.
    for _ in number_init:
        sum_number += int(_)
    return sum_number


def number_count(number_init):
    count_number = 0
    for _ in number_init:
        count_number += 1
    return count_number


number = input('Введите целое положительное число: ')

number_summ_dig = number_sum(number)
number_count_dig = number_count(number)

print('\nСумма цифр:', number_summ_dig)
print('Кол-во цифр в числе:', number_count_dig)
print('Разность суммы и кол-ва цифр:', number_summ_dig - number_count_dig)

'''
# , предлагаю попробовать сократить количество вызовов наших функций.
#  т.к. каждый вызов функции это отдельное действие для python, которое создаёт нагрузку на код.
#  Возможно мы сможем создать переменные с возвратом функций и использовать в работе их? =)
'''

# зачёт!
