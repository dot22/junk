string = 'shacnidw'
word1 = ''
word2 = ''
position = 0

for letter in string:
    position += 1
    if position % 2 == 1:
        word1 = word1 + letter
    else:
        word2 = letter + word2

print(word1 + word2)
