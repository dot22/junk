number = int(input('Введите количество пар слов: '))
syn_dict = {}

for i_num in range(1, number + 1):
    print(i_num, 'пара: ', end='')
    string = input('').lower().split(' - ')
    syn_dict[string[0]] = string[1]
    syn_dict[string[1]] = string[0]

while True:
    word = input('Введите слово: ').lower()
    if word in syn_dict:
        print('Синоним:', syn_dict[word])
        break
    else:
        print('Такого слова в словаре нет.')

# зачёт!
