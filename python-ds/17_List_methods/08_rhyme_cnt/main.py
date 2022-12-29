men = int(input('Количество людей: '))
number = int(input('Какое количество в считалке? '))

print('Значит, выбывает каждый', number, 'человек')

list_men = [i_men for i_men in range(1, men + 1)]

for _ in range(men - 1):
    print('\nТекущий круг людей:', sorted(list_men))
    print('Начало счета с номера', list_men[0])
    for _ in range(number):
        shifted_num = list_men[0]
        list_men.append(shifted_num)
        list_men.remove(shifted_num)
    print('Выбывает человек под номером', list_men[-1])
    list_men.pop(-1)

print('\nОстался человек под номером', list_men[0])

# зачёт!
