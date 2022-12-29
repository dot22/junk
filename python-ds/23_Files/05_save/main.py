import os


def generate_path(path):
    list_path = path.split(' ')
    generated_path = os.path.sep
    for i_list in list_path:
        generated_path = os.path.join(generated_path, i_list)
    return generated_path


def write_file(folder, file, text):
    if os.path.exists(os.path.join(folder, file)):
        rewrite = input('Вы действительно хотите перезаписать файл? ')
        if rewrite == 'да':
            file_to_write = open(os.path.join(folder, file), 'w')
            file_to_write.write(text)
            file_to_write.close()
            print('Файл успешно перезаписан!')
        else:
            print('Существующий файл не изменен')
    else:
        file_to_write = open(os.path.join(folder, file), 'w')
        file_to_write.write(text)
        print('Файл успешно сохранен!')
        file_to_write.close()
    return


user_text = input('Введите строку: ')
folders_list = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел): ')
folders_path = generate_path(folders_list)
if os.path.exists(folders_path):
    file_name = input('Введите имя файла: ')
    write_file(folders_path, file_name, user_text)
    print('Содержимое файла:')
    file = open(os.path.join(folders_path, file_name), 'r')
    print_file = file.read()
    print(print_file)
    file.close()
else:
    print('Такого каталога не существует')
