file = open('words.txt', 'r')
palindrom = 0

try:
    for i_word in file:
        if i_word.endswith('\n'):
            i_word = i_word[:-1]
        if not i_word.isalpha():
            raise TypeError
        else:
            if i_word == i_word[::-1]:
                palindrom += 1
except TypeError:
    print('В слове {} содержится цифра'.format(i_word))

print('Число палиндромов:', palindrom)
