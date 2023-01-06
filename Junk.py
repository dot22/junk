# string_1 = 'Привет!'
# string_2 = 'Как дела? Что делаешь?'
string_1 = 'Хм!!'
string_2 = '?'

print('Первое сообщение:', string_1)
print('Второе сообщение:', string_2)

if string_1.count('!') + string_1.count('?') > string_2.count('!') + string_2.count('?'):
    print(string_1 + string_2)
elif string_1.count('!') + string_1.count('?') < string_2.count('!') + string_2.count('?'):
    print(string_2 + string_1, sep=' ')
else:
    print('Ой!')
