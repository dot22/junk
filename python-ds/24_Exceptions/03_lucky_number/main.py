import random


errors = [
    'Не повезло',
    'Вас постигла неудача',
    'Повезет в следующий раз'
]

sum_number = 0

with open('out_file.txt', 'w') as out_file:
    try:
        while sum_number < 777:
            number = int(input('Введите число: '))
            sum_number += number
            if random.randint(1, 13) == 13:
                raise Exception
            out_file.write(str(number) + '\n')
        print('Вы успешно выполнили условие для выхода из порочного цикла!')
    except Exception:
        print(random.choice(errors))

with open('out_file.txt', 'r') as out_file:
    print('\nСодержимое файла out_file.txt:')
    print(out_file.read())
