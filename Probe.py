import random


original_list = [random.randint(0, 99) for x in range(10)]
print('Оригинальный список:', original_list)

# print('\nВариант 1')
# new_list_1 = []
# for i_index in range(0, 10, 2):
#     list_for_add = (original_list[i_index], original_list[i_index + 1])
#     new_list_1.append(list_for_add)
# print(new_list_1)

print('\nВариант 2')
new_list_2 = []
for i_count, i_data in enumerate(original_list):
    print(i_count, i_data)

