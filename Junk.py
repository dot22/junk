def print_tree(some_dict, tab_level=0):
    comma_level = len(some_dict) - 1
    for i_key, i_value in some_dict.items():
        tab_level += 1
        if not isinstance(some_dict[i_key], dict):
            if comma_level > 0:
                print(tab_level * "\t", "'", i_key, "': '", i_value, "',", sep='')
            else:
                print(tab_level * "\t", "'", i_key, "': '", i_value, "'", sep='')
        else:
            print(tab_level * "\t", "'", i_key, "': {", sep='')
            some_tree = some_dict[i_key]
            print_tree(some_tree, tab_level)
            if comma_level > 0:
                print(tab_level * "\t", "},")
            else:
                print(tab_level * "\t", "}")
        tab_level -= 1
        comma_level -= 1

# site = {
#     'html': {
#         'head': {
#             'title': 'Куплю/продам телефон недорого'
#         },
#         'body': {
#             'h2': 'У нас самая низкая цена на iphone',
#             'div': 'Купить',
#             'p': 'Продать'
#         }
#     }
# }

# print_tree(site)

amount_site = int(input('Сколько сайтов: '))
list_sites = []

for i_count in range(amount_site):
    name_site = input('Введите название продукта для нового сайта: ')
    list_sites.append(name_site)
    print()
    for i_name in list_sites:
        print('Сайт для ', i_name, ':', sep='')
        site = {
            'html': {
                'head': {
                    'title': 'Куплю/продам телефон недорого'
                },
                'body': {
                    'h2': 'У нас самая низкая цена на телефон',
                    'div': 'Купить',
                    'p': 'Продать'
                }
            }
        }
        print_tree(site)
