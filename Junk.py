def print_tree(some_dict, tab_level=0):
    for i_key, i_value in some_dict.items():
        # tab_level = 0
        if not isinstance(some_dict[i_key], dict):
            tab_level += 1
            print(tab_level * "\t", "'", i_key, "': '", i_value, "'", sep='')
            tab_level -= 1
        else:
            tab_level += 1
            print(tab_level * "\t", "'", i_key, "': {", sep='')
            sub_tree = some_dict[i_key]
            print_tree(sub_tree, tab_level)
            print("}")
            tab_level -= 1


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
