import zipfile

zip_file = zipfile.ZipFile('voyna-i-mir.zip')
path = zipfile.Path(zip_file, at='voyna-i-mir.txt')
content = path.read_text(encoding='utf-8')

dict_letters = {}

for i_letter in content:
    if i_letter.isalpha():
        if i_letter not in dict_letters:
            dict_letters[i_letter] = 1
        else:
            dict_letters[i_letter] += 1

sorted_dict = {}
sorted_keys = sorted(dict_letters, key=dict_letters.get)

for i_key in sorted_keys:
    sorted_dict[i_key] = dict_letters[i_key]

print('Частота встречаемости букв по возрастанию:')
for i_item in sorted_dict:
    print('Буква', i_item, '-', sorted_dict[i_item])
