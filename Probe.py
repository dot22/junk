def count_letters(some_text):
    count_num = 0
    count_let = 0
    number = input('What number: ')
    letter = input('What letter: ')
    for i in some_text:
        if i == number:
            count_num += 1
        elif i == letter:
            count_let += 1
    print('Number', number, 'is:', count_num)
    print('Letter', letter, 'is', count_let)


text = input('Enter some text: ')
count_letters(text)
