def search_key(dbase, key, deep):
    if deep != 0:
        if key in dbase:
            return dbase[key]

        for sub_base in dbase.values():
            if isinstance(sub_base, dict):
                result = search_key(sub_base, key, deep)
                deep -= 1
                print(deep)
                if result:
                    break
        else:
            result = None
    else:
        print('Достигнута максимальная глубина')
        return

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

user_deep = int(input('На какую глубину искать (по-умолчанию - без ограничения)? ') or '-1')

value = search_key(site, user_key, user_deep)

if value:
    print(value)
else:
    print('Такого ключа в структуре базы нет')
