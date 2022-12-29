word = input('Введите слово: ')
unique_letters = len(word)

for letter in word:
    count = 0
    for check_letter in word:
        if letter == check_letter:
            count += 1
    if count > 1:
        unique_letters -= 1

print('Количество уникальных букв:', unique_letters)

# зачёт!
