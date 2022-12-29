vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']

text = input('Введите текст: ')
# text = 'Нужно отнести кольцо в Мордор!'

vowels_list = [i_letter for i_letter in text if i_letter in vowels]

print('Список гласных букв:', vowels_list)
print('Длина списка:', len(vowels_list))

# зачёт!
