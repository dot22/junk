text = input('Введите строку: ')
new_text = ''

text_list = list(text)
new_text_list = []

count = 0

for i in text_list:
    if i != ':':
        new_text_list.append(i)
    else:
        count += 1
        new_text_list.append(';')

for j in new_text_list:
    new_text += j

print('Исправленная строка:', new_text)
print('Количество замен:', count)

