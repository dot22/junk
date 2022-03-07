def ask_user(question, errata='Неправильный ввод', count=4):
    while True:
        question = input('Создать файл? ').lower()
        if question == 'да':
            return 1
        elif question == 'нет':
            return 0
        else:
            print(errata)
        count -= 1
        if count == 0:
            print('Количество попыток исчерпано')
            break




