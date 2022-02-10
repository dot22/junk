text = input('Введите текст: ')
original_dict = {}

for i_sym in text:
    if i_sym in original_dict:
        original_dict[i_sym] += 1
    else:
        original_dict[i_sym] = 1

print(original_dict)
