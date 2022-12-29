amount = int(input('Количество видеокарт: '))
card_list = []
new_card_list = []
generation = 0
generation_old = 0

for serial in range(1, amount + 1):
    print(serial, 'Видеокарта:', end=' ')
    model = int(input())
    card_list.append(model)
    generation = int(model) % 100
    if generation_old < generation:
        generation_old = generation

for card in card_list:
    if int(card) % 100 < generation_old:
        new_card_list.append(card)

print('\nСтарый список видеокарт:', '[', *card_list, ']', sep=' ')
print('Новый список видеокарт:', '[', *new_card_list, ']', sep=' ')

# зачёт!
