while True:
    grats_template = input('Введите шаблон поздравления {name} и {age}: ')
    if '{name}' in grats_template and {age} in grats_template:
        break
    else:
        print('Ошибка. Отсутствует одна или две конструкции')

names_list = input('Список людей через запятую: ').split(', ')
ages_str = 
for i_name in names_list:
    print(grats_template.format(name=i_name))