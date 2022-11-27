password = 5555

while True:
    print('Компьютер заблокирован. Вернёшь скейт — скажу код разблокировки!')
    question = int(input('Введите код: '))
    if question == password:
        print('Код верный, завершаю работу...')
        break
