nums_count = int(input('Количество чисел в списке: '))
nums_list = []

for i_num in range(nums_count):
    print('Введите', i_num + 1, 'число:', end=' ')
    nums_list.append(int(input('')))

# print(nums_list)

divider = int(input('Введите делитель: '))

index_sum = 0

for i_num in range(nums_count):
    if nums_list[i_num] % divider == 0:
        print('Индекс числа ', nums_list[i_num], ': ', i_num, sep='')
        index_sum += i_num

print('Сумма индексов:', index_sum)
