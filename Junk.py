# def matryoshka(n):
#     if n == 1:
#         print('Матрешечка')
#     else:
#         print('Верх матрешки n=', n)
#         matryoshka(n - 1)
#         print('Низ матрешки n=', n)
#
# matryoshka(5)

def print_tree(some_dict, level=1):
    for i_key, i_value in some_dict.items():
        if isinstance(some_dict[i_key], dict):
            print(i_key)
            sub_tree = some_dict[i_key]
            print_tree(sub_tree, level)
            level += 1
            print(level)
        else:
            print(i_key, i_value)


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

print_tree(site)

