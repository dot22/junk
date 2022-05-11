import os

def find_file(cur_path, file_name):
    print('переходим ', cur_path)

    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        print('    смотрим', path)

        if file_name == i_elem:
            return path
        elif os.path.isdir(path):
            print('Это директория')
            result = find_file(path, file_name)
            if result:
                break
    else:
        result = None

    return result


file_path = find_file(os.path.abspath(os.path.join('..', '..', 'Obsidian')), 'TODO.md')
history_file = open('search_history.txt', 'a')
if file_path:
    print('Абсолютный путь к файлу:', file_path)
    history_file.write(file_path)
    history_file.close()
else:
    print('Файл не найден')
