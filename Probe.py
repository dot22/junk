peoples = 5
order = 7
start = 0

print('\nКоличество человек:', peoples)
print('Какое число в считалке?', order)
print('Значит, выбывает каждый ', order, '-й человек', sep='')
print()

peoples_list = list(range(1, peoples + 1))

while len(peoples_list) > 1:
    print('Текущий круг людей:', peoples_list)
    print('Начало счета с номера', peoples_list[start])
    shift = start + order % len(peoples_list) - 1
    print('Выбывает человек под номером', peoples_list[shift])
    peoples_list.remove(peoples_list[shift])
    start = shift
    print(start)

    print()

print('Остался человек под номером', peoples_list[0])
