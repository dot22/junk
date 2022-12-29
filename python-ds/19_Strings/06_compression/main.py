string = input('Введите кодируемую строку: ')
# string = 'aaAAbbсaaaA'
# string = 'aaaabbсaa'
code = ''
count = 1

for i_sym in range(len(string) - 1):
    if string[i_sym] != string[i_sym + 1]:
        code += string[i_sym] + str(count)
        count = 1
    else:
        count += 1

code += string[i_sym + 1] + str(count)

print('Закодированная строка:', code)

# зачёт!
