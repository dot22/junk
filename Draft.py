names_list = []

while True:
    try:
        name = input('Введите имя: ')
        if name.lower() == 'error':
            raise BaseException('Программа сломана')
        if not name.isalpha():
            raise TypeError
        names_list.append(name)
        if len(names_list) == 5:
            print('Место закончилось')
            break
    except TypeError:
        print('Неправильный ввод')
    except BaseException:
        names_list = []
        print('Введено стоп-слово')
        raise ValueError('Пожалуйста, не вводите стоп-слово')

names_file = open('names.txt', 'w')
names_file.write('\n'.join(names_list))
names_file.close()
print('Программа закончена. Запись завершена')
