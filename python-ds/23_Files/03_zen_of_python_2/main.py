zen_file_read = open('zen.txt', 'r')

letters_count = 0
words_count = 0
strings_count = 0
letters_dict = {}

for i_string in zen_file_read:
    strings_count += 1
    for i_word in i_string.split(' '):
        words_count += 1
        for i_letter in i_word:
            if i_letter.isalpha():
                letters_count += 1
                if i_letter.lower() in letters_dict:
                    letters_dict[i_letter.lower()] += 1
                else:
                    letters_dict[i_letter.lower()] = 1

print('Количество букв в файле:', letters_count)
print('Количество слов в файле:', words_count)
print('Количество строк в файле:', strings_count)
print('Наиболее редкая буква:', min(letters_dict, key=letters_dict.get))

zen_file_read.close()
