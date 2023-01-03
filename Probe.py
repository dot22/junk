text = input('Введите строку: ')
sym_number = int(input('Номер символа: '))

text_list = list(text)
count = 0

print()
print('Символ слева:', text_list[sym_number - 2])
print('Символ справа:', text_list[sym_number])

if text_list[sym_number - 2] == text_list[sym_number - 1] == text_list[sym_number]:
    print('\nЕсть еще два таких символа')
elif text_list[sym_number - 2] == text_list[sym_number - 1] or text_list[sym_number - 1] == text_list[sym_number]:
    print('\nЕсть ровно один такой же символ')
else:
    print('\nТаких же символов нет')
