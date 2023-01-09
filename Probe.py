main_list = [1, 5, 3]
ext_list_b = [1, 5, 1, 5]
ext_list_c = [1, 3, 1, 5, 3, 3]

main_list.extend(ext_list_b)
print('Количество цифр 5 при объединении:', main_list.count(5))

while 5 in main_list:
    main_list.remove(5)

main_list.extend(ext_list_c)
print('Количество цифр 3 при втором объединении:', main_list.count(3))

print('Итоговый список:', main_list)
