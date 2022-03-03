some_string = 'abcd'
some_tuple = (10, 20, 30, 40)

print('Строка:', some_string)
print('Кортеж чисел:', some_tuple)

print('\nРезультат:')
result = ((some_string[i], some_tuple[i]) for i in range(len(some_string)))
print(result)
for i_index in result:
    print(i_index)
