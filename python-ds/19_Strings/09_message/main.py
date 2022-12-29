def reverse_word(word):
    return word[-1::-1]


text = input('Сообщение: ')
# text = 'Это задание очень! простое.'
# text = 'Хотя ,. возм:ожно и нет.'

i_word = ''
new_text = ''

for i_sym in text:
    if i_sym.isalpha():
        i_word += i_sym
    else:
        new_text += reverse_word(i_word) + i_sym
        i_word = ''

print('Новое сообщение:', new_text)

# зачёт!
