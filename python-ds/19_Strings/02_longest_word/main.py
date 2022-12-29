checked_string = input('Введите строку: ')
checked_list = checked_string.split(' ')
longest_word = ''

for i_word in checked_list:
    if len(i_word) > len(longest_word):
        longest_word = i_word

print('Самое длинное слово в строке:', longest_word)

# зачёт!
