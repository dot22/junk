h_sentence = input('Введите текст: ')
# h_sentence = 'Honest Robin Hood hide his hitted face'

print('Изначальная фраза:', h_sentence)

first_order = h_sentence.index('h')
last_order = h_sentence.rindex('h')
print('Перевернытый срез:', h_sentence[last_order:first_order - 1:-1])

# зачёт!
