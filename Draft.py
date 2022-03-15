def search_key(dbase, key):
    if key in dbase:
        return dbase[key]

    for sub_base in dbase.values():
        if isinstance(sub_base, dict):
            result = search_key(sub_base, key)
            if result:
                break
    else:
        result = None

    return result


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

user_key = input('Какой ключ ищем? ')
user_deep = int(input('На какую глубину искать (по-умолчанию - без ограничения)? '))

value = search_key(site, user_key)
if value:
    print(value)
else:
    print('Такого ключа в структуре базы нет')
