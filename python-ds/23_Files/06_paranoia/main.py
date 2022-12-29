import string


read_file = open('text.txt', 'r')
crypt_file = open('cipher_text.txt', 'w')
count = 1
for i_line in read_file:
    crypt_line = ''
    for i_letter in list(i_line[:-1]):
        letter_index = string.ascii_letters.index(i_letter)
        crypt_line += string.ascii_letters[letter_index + count]
    crypt_line += '\n'
    crypt_file.write(crypt_line)
    count += 1

crypt_file.close()
read_file = open('text.txt', 'r')
crypt_file = open('cipher_text.txt', 'r')
data_encrypt = read_file.read()
data_crypt = crypt_file.read()
print('Содержимое файла text.txt:')
print(data_encrypt)
print()
print('Содержимое файла cipher_text.txt:')
print(data_crypt)

read_file.close()
crypt_file.close()