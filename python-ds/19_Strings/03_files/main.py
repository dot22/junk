file_name = input('Имя файла: ')
forbidden_list = list('@№$%^&*()')

if not (file_name.endswith('.txt') or file_name.endswith('.docx')):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
elif any(file_name.startswith(f_sym) for f_sym in forbidden_list):
    print('Ошибка: название начинается на один из специальных символов')
else:
    print('Файл назван верно.')

# зачёт!
