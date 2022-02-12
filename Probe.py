import random


number = int(input('Введите максимальное число: '))
right_number = random.randint(1, number)
number_set = {str(i) for i in range(1, number + 1)}

while True:
    print('\nНужное число есть среди вот этих чисел: ', end='')
    search_list = set(input().split(' '))
    if len(number_set) == 1:
        print('осталось одно число')
    elif

    if right_number in
for i in search_list:
    number_set.discard(i)
print(number_set)