number = int(input('Введите максимальное число: '))
number_set = {str(i) for i in range(1, number + 1)}

while True:
    if len(number_set) == 1:
        print('Нужное число найдено:', *number_set)
        break

    print('\nНужное число есть среди вот этих чисел: ', end='')
    search = input()
    if search == 'Помогите!':
        print('Артем мог загадать следующие числа:', ' '.join(sorted(number_set)))
        break
    else:
        search_set = set(search.split(' '))

    answer = input('Ответ Артема: ')
    if answer == 'Да':
        number_set = number_set.intersection(search_set)
    elif answer == 'Нет':
        number_set = number_set.difference(search_set)

# зачёт!
