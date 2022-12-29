word = input('Введите слово: ')
word_list = []
reverse_list = []

for letter in word:
    word_list.append(letter)

for order in range(len(word_list) - 1, -1, -1):
    reverse_list.append(word_list[order])

if word_list == reverse_list:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')

# зачёт!
