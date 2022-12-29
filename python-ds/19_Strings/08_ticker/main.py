first_string = input('Первая строка: ')
# first_string = 'abcd'
second_string = input('Вторая строка: ')
# second_string = 'cdab'
# second_string = 'cdba'

test_string = second_string * 2

if test_string.find(first_string) == -1:
    print('\nПервую строку нельзя получить из второй с помощью циклического сдвига.')
else:
    print('\nПервая строка получается из второй со сдвигом', test_string.find(first_string))

# зачёт!
