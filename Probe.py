site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

copy_sites = int(input('Сколько будет сайтов: '))
for _ in range(copy_sites):
    name_site = input('Введите название продукта для нового сайта: ')
    print('Сайт для', name_site, ':')
    print(site)


