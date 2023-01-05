films = [
    'Крепкий орешек', 'Назад в будущее', 'Таксист',
    'Леон', 'Богемская рапсодия', 'Город грехов',
    'Мементо', 'Отступники', 'Деревня',
    'Проклятый остров', 'Начало', 'Матрица'
]

personal_top = []
while True:
    print('Ваш текущий топ фильмов:', personal_top)
    film = input('Название фильма: ')
    if film not in films:
        print('Такого фильма нет в фильмотеке')
    else:
        print('Команды: добавить, вставить, удалить')
        action = input('Введите команду: ')
        if action == 'добавить':
            if film in personal_top:
                print('Этот фильм уже есть в вашем списке.')
            else:
                personal_top.append(film)
        elif action == 'вставить':
            if film in personal_top:
                print('Этот фильм уже есть в вашем списке.')
            else:
                position = int(input('Введите позицию: '))
                personal_top.insert(position - 1, film)
        elif action == 'удалить':
            if film not in personal_top:
                print('Такого фильма нет в вашем списке')
            else:
                personal_top.remove(film)
