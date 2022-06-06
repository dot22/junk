def read():
    chat_read = open('chat.txt', 'r', encoding='utf-8')
    for i_line in chat_read:
        print(i_line, end='')
    chat_read.close()
    return


def write():
    chat_write = open('chat.txt', 'a', encoding='utf-8')
    text = input('Отправить сообщение: ')
    text_to_chat = (name + ': ' + text + '\n')
    chat_write.write(text_to_chat)
    chat_write.close()
    return


name = input('Введите имя: ')

print('Привет,', name)

while True:
    answer = input('\nВыберите действие: 1 - просмотреть текущий текст чата, 2 - отправить сообщение: ')
    if answer == '1':
        read()
    elif answer == '2':
        write()
    else:
        print('Ошибка в выборе действия')
