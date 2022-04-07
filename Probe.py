import os

def find_file(path,file):
    if os.path.exists(os.path.join(path, file)):
        print(os.path.join(path, file))

    if os.path.isdir(os.path.join(path, file)):
        sub_dir = os.path.join(path, file)
        find_file(sub_dir, file)

# abs_path = 'd:\yandex\git'
abs_path = 'd:\yandex\git\junk.w'
file_name = 'Junk.py'

find_file(abs_path, file_name)
