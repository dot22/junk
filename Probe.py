import os


def read_file(path, file):
    for i_elem in os.listdir(path):
        if i_elem == file:


    if os.path.exists(os.path.join(path, file)):
        print(os.path.join(path, file))
        file_read = open(os.path.join(path, file), 'r')
        data = file_read.read()
        print(data)
        return file_read.close()
        # return print(data)
    for i_list in os.listdir(path):
        if os.path.isdir(os.path.join(path, i_list)):
            sub_path = os.path.join(path, i_list)
            read_file(sub_path, file)


path_search = '/home/dot/Yandex/Obsidian'
file_search = 'Template.md'

read_file(path_search, file_search)
