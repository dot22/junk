num = int(input('Введите количество чисел в списке: '))
print()

num_list = [int(input('Введите число: ')) for _ in range(num)]
print('Изначальный список:', num_list)

# simple version
# for _ in range(num_list.count(0)):
#     num_list.remove(0)
#     num_list.append(0)

## or
# version with list comprehensions
num_list = ([num_list[i] for i in range(num) if num_list[i] != 0]) + ([0 for _ in range(num_list.count(0))])
print('\nПреобразованный список:', num_list)

num_list = num_list[:-num_list.count(0)]
print('Сжатый список:', num_list)

# зачёт!
