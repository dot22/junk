phone_book = {}

while True:
    action = input('\nВведите действие:\n"Добавить контакт" (нажмите 0)\n\tили\n"Поиск человека по фамилии" (нажмите 1): ')
    if action == '0':
        person = tuple(input('Имя, Фамилия: ').split(' '))
        if person in phone_book.keys():
            print('Такой контакт уже есть в телефонной книге')
        else:
            phone_number = input('Номер телефона: ')
            phone_book[person] = phone_number
        print(phone_book)
    elif action == '1':
        search_name = input('Введите фамилию для поиска')
        for i_name in phone_book:
            if search_name in i_name:
                print(i_name, phone_book[i_name])
    else:
        break