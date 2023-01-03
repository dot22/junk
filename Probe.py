dogs_count = int(input('Количество собак: '))
dogs_list = []

for i_dog in range(dogs_count):
    print('Рейтинг собаки', i_dog + 1, '-', end=' ')
    dogs_list.append(int(input('')))

print('\nНеверный рейтинг собак:')
print(dogs_list)

min_dog = 0
max_dog = 0

for i_dog in range(dogs_count):
    if dogs_list[min_dog] > dogs_list[i_dog]:
        min_dog = i_dog
    if dogs_list[max_dog] < dogs_list[i_dog]:
        max_dog = i_dog

# print(min_dog, max_dog)
dogs_list[min_dog], dogs_list[max_dog] = dogs_list[max_dog], dogs_list[min_dog]
print('\nВерный рейтинг собак:')
print(dogs_list)
