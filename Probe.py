girls = int(input('How many girls? '))
boys = int(input('How many boys? '))

if (girls > 2 * boys) or (boys > 2 * girls):
    print('Решения нет')
elif girls >= boys:
    print((girls - boys) * 'GBG' + (boys - (girls - boys)) * 'BG')
else:
    print((boys - girls) * 'BGB' + (girls - (boys - girls)) * 'GB')
