def shifted_word(some_word):
    return [(abc_string[abc_string.index(i_letter) + 3]
             if abc_string.index(i_letter) < 30
             else abc_string[abc_string.index(i_letter) - 30])
            for i_letter in some_word]


abc_string = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
text_string = input('Введите сообщение: ')
text_list = text_string.split()
shift = int(input('Введите сдвиг: '))

shifted_list = [shifted_word(i_word) for i_word in text_list]
shifted_text = ' '.join([''.join(shifted_list[i]) for i in range(len(shifted_list))])

print('Зашифрованное сообщение: ', shifted_text)

# зачёт!
