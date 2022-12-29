countries = int(input('Количество стран: '))
countries_dict = {}

for c_num in range(1, countries + 1):
    print(c_num, 'страна: ', end='')
    country_list = input().split(' ')
    countries_dict[country_list[0]] = country_list[1:]

for i_city in range(1, 4):
    print('\n', i_city, 'город: ', end='')
    city = input()
    for i_country in countries_dict:
        if city in countries_dict[i_country]:
            print('Город', city, 'расположен в стране', i_country)
            break
    else:
        print('По городу', city, 'данных нет.')

# зачёт!
