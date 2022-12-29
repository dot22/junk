class_1 = []
class_2 = []
class_common = []

for i_height in range(160, 172, 2):
    class_1.append(i_height)
print('Список по росту 1-й класс:', class_1)

for i_height in range(162, 183, 3):
    class_2.append(i_height)
print('Список по росту 2-й класс:', class_2)

class_common = class_1 + class_2
print('Список без сортировки объединенный класс:', class_common)

for i_num in range(len(class_common) - 1):
    for i_change in range(i_num, len(class_common) - 1):
        if class_common[i_num] > class_common[i_change]:
            class_common[i_num], class_common[i_change] = class_common[i_change], class_common[i_num]
print('Список по росту объединенный класс', class_common)

# зачёт!
