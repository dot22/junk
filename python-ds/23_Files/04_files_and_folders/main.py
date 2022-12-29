import os


def folder_info(path):
    for i_elem in os.listdir(path):
        if os.path.isfile(os.path.join(path, i_elem)):
            info_list[1] += 1
            info_list[2] += os.path.getsize(os.path.join(path, i_elem))
        elif os.path.isdir(os.path.join(path, i_elem)):
            info_list[0] += 1
            sub_path = os.path.join(path, i_elem)
            folder_info(sub_path)
    return


folder_path = input('Введите полный путь до каталога: ')
info_list = [0, 0, 0]
folder_info(folder_path)

print('Размер каталога (в Кб):', info_list[2] / 1024)
print('Количество подкаталогов:', info_list[0])
print('Количество файлов:', info_list[1])
