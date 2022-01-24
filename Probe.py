def crypt(symbol):
    return abc[(abc.index(symbol) + shift) % 33]

abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
text = input('Введите шифрумое предложение: ')
shift = int(input('Введите сдвиг: '))

crypt_text = ''.join([crypt(i_sym) if i_sym != ' ' else ' ' for i_sym in text])

print(crypt_text)