guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('Сейчас на вечеринке', len(guests), 'человек:', guests)
    query = input('Гость пришел или ушел? ')
    if query == 'Пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break
    elif query == 'ушел':
        name = input('Имя гостя: ')
        if name in guests:
            guests.remove(name)
            print('Пока, ', name, '!', sep='')
        else:
            print('Такого имени нет среди гостей')
    elif query == 'пришел':
        name = input('Имя гостя: ')
        if name in guests:
            print('Такое имя уже есть в списке гостей')
        elif len(guests) < 6:
            print('Привет, ', name, '!', sep='')
            # ex_TODO, если гость уже есть в списке, то не добавляем. Иначе, задвоим гостей.
            # UPDATE: Уникальность имен гостей не ставилась в условиях задачи.
            guests.append(name)
        else:
            print('Прости, ', name, ', но мест нет.', sep='')
    else:
        print('Ответ непонятен. Повторите еще раз')

# зачёт!
