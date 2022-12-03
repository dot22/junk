string = input('Enter the string: ')
word = 0
word_max = 0

for letter in string:
    if word_max < word:
        word_max = word
    if letter != ' ':
        word += 1
    else:
        word = 0

print(word_max)