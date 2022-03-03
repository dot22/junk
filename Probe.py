## test data
# score_dict = {
#     1: ('69485', 'Jack'),
#     2: ('95715', 'qwerty'),
#     3: ('95715', 'Alex'),
#     4: ('83647', 'M'),
#     5: ('197128', 'qwerty'),
#     6: ('95715', 'Jack'),
#     7: ('93289', 'Alex'),
#     8: ('95715', 'Alex'),
#     9: ('95715', 'M')
# }

count = int(input('Сколько записей вносится в протокол? '))
score_dict = {}

print('Записи (результат и имя):')

## составляем словарь из записей состоявшихся игр
for i_count in range(1, count + 1):
    print(i_count, 'запись: ', end='')
    record = tuple(input().split(' '))
    score_dict[i_count] = record

## сортируем очки состоявшихся игр в обратном порядке
score_rates = sorted([int(i_value[0]) for i_key, i_value in score_dict.items()], reverse=True)

top_list = {}
top_users = []

## перебирая поочередно список очков состоявшихся игр, распределяем игры по убыванию счета в игре
## удаляя дублирующиеся имена игроков
for i_rate, i_score in enumerate(score_rates):
    for i_value in score_dict.values():
        user_score = i_value[0]
        user_name = i_value[1]
        if i_score == int(user_score) and user_name not in top_users:
            top_list[i_rate + 1] = (user_name, user_score)
            top_users.append(user_name)
            break

## выводим на печать первые три призовых места
print('\nИтоги соревнований:')
for i_top in range(1, 4):
    print(i_top, ' место. ', top_list.get(i_top)[0], ' (', top_list.get(i_top)[1], ')', sep='')
