container_list = []
container_amount = int(input('Количество контейнеров: '))

for _ in range(container_amount):
    container_mass = int(input('Введите вес контейнера: '))
    while True:
        if container_mass > 200:
            print('Вес контейнера не должен превышать 200. Повторите ввод.')
            container_mass = int(input('Введите вес контейнера: '))
        else:
            break
    container_list.append(container_mass)

new_container_mass = int(input('Введите вес нового контейнера: '))
new_container_order = 1

for order in range(len(container_list)):
    if new_container_mass <= container_list[order]:
        new_container_order += 1

print('Номер, который получит новый контейнер:', new_container_order)

# зачёт!
