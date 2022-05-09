import os


def find_file(path, file):
    if os.path.exists(os.path.join(path, file)):
        print(os.path.join(path, file))
    for i_elem in os.listdir(path):
        if os.path.isdir(os.path.join(path, i_elem)):
            sub_path = os.path.join(path, i_elem)
            find_file(sub_path, file)
            # print(i_elem)


path_search = '/home/dot/Yandex/Obsidian'
file_search = 'Template.md'

find_file(path_search, file_search)