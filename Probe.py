site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

def find_key(structure, search):
    if search in structure:
        return structure[search]

    for substructure in structure.values():
        print(substructure)
        if isinstance(substructure, dict):



key = input('Какой ключ ищем? ')
value = find_key(site, key)
if value:
    print(value)
else:
    print('Такого ключа нет')