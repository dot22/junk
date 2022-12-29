friends = int(input('Количество друзей: '))
debets = int(input('Долговых расписок: '))
debet_list = []

for _ in range(friends):
    debet_list.append(0)

for i_debet in range(debets):
    print('\n', i_debet + 1, 'расписка')
    who = int(input('Кому: '))
    whom = int(input('От кого: '))
    how_much = int(input('Сколько: '))
    debet_list[who - 1] -= how_much
    debet_list[whom - 1] += how_much

print('\nБаланс друзей:')

for i_order in debet_list:
    print(debet_list.index(i_order) + 1, ':', i_order)

# зачёт!
