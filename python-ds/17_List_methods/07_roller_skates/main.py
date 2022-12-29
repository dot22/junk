amount = 0

N = int(input('Сколько всего коньков: '))
list_size = []

for i_scale in range(1, N + 1):
    print('Размер', i_scale, 'пары:', end=' ')
    size = int(input())
    list_size.append(size)
list_size.sort()

K = int(input('\nСколько пришло людей: '))
list_men = []

for i_num in range(1, K + 1):
    print('Размер ноги', i_num, 'человека:', end=' ')
    num = int(input())
    list_men.append(num)
list_men.sort()

for i_men in list_men:
    for i_size in list_size:
        if i_size == i_men:
            list_size.remove(i_size)
            amount += 1
            break

print('\nНаибольшее количество людей на коньках:', amount)

# зачёт!