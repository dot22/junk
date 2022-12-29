import string
import operator


dict_letters = {}
total_number = 0
file = open('text.txt', 'r')
analys = open('analysis.txt', 'w')
read_file = file.read()

for i_letter in read_file:
    if i_letter in string.ascii_letters:
        total_number += 1
        if i_letter.lower() not in dict_letters:
            dict_letters[i_letter.lower()] = 1
        else:
            dict_letters[i_letter.lower()] += 1

list_letters = [x for x in dict_letters.items()]

list_letters = sorted(list_letters, key=operator.itemgetter(1, 0))

set_for_sorting = set()
for i_elem in dict_letters:
    set_for_sorting.add(dict_letters[i_elem])
reverse_list = list(set_for_sorting)[::-1]

for i_list in reverse_list:
    for i_letter in list_letters:
        if i_list == i_letter[1]:
            analys.write(i_letter[0] + ' ' + str(round((i_letter[1] / total_number), 3)) + '\n')

file.close()
analys.close()

file = open('text.txt', 'r')
analys = open('analysis.txt', 'r')

print('Содержимое файла text.txt')
print(file.read())
print()
print('Содержимое файла analysis.txt')
print(analys.read())

file.close()
analys.close()
