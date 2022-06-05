name = input('Введите имя: ')

while True:
    answer = input('Выберите действие: 1 - просмотреть текущий текст чата, 2 - отправить сообщение: ')
    if answer == '1':
        chat = open('chat.txt', 'r')
        for i_line in chat:
            print(i_line)
    else:
        print('выход')