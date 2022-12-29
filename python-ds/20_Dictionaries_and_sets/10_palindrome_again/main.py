test_string = input('Введите строку: ')
text_dict = {}
count = 0

for i_sym in test_string:
    if i_sym in text_dict:
        text_dict[i_sym] = text_dict.get(i_sym) + 1
    else:
        text_dict[i_sym] = 1

for i_value in text_dict.values():
    if i_value % 2 == 1:
        count += 1

if count <= 1:
    print('Можно сделать палиндром')
else:
    print('Нельзя сделать палиндром')

# зачёт!
