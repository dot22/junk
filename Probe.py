guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('Сейчас на вечеринке', len(guests), 'человек:', guests)
    question = input('Гость пришел или ушел? ')
    if question == 'пора спать':
        print('\nВечеринка закончилась, все легли спать.')
        break
    elif question == 'пришел':
        name = input('Имя гостя:')
        if len(guests) >= 6:
            print('Прости, ', name, ', но мест нет.', sep='')
        else:
            print('Привет,', name)
            guests.append(name)
    else:
        name = input('Имя гостя: ')
        print('Пока,', name)
        guests.remove(name)
