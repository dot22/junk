films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

favorite_list = []
number = int(input('Сколько фильмов хотите добавить? '))

for _ in range(number):
    print('Введите название фильма: ', end='')
    film = input()
    for name in films:
        if film == name:
            favorite_list.append(name)
            flag = True  # строка кода получилась лишней.
            break
    else:
        print('Ошибка: фильма', film, 'у нас нет :(')

print('Ваш список любимых фильмов: ', end='')
print(*favorite_list, sep=', ')

# зачёт!
