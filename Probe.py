word_list = []
word_count_list = [0, 0, 0]

for i in range(1, 4):
    print('Введите', i, 'слово:', end=' ')
    word_list.append(input())

# print(word_list)

while True:
    text = input('Слово из текста: ')
    if text == 'end':
        break
    for i in range(3):
        if text == word_list[i]:
            word_count_list[i] += 1

# print(word_count_list)

print('\nПодсчет слов в тексте')

for i in range(3):
    print(word_list[i], ': ', word_count_list[i], sep='')
