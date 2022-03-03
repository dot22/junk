# count = int(input('Сколько записей вносится в протокол? '))
# score_dict = {}

## test data
score_dict = {
    1: ('69485', 'Jack'),
    2: ('95715', 'qwerty'),
    3: ('95715', 'Alex'),
    4: ('83647', 'M'),
    5: ('197128', 'qwerty'),
    6: ('95715', 'Jack'),
    7: ('93289', 'Alex'),
    8: ('95715', 'Alex'),
    9: ('95715', 'M')
}

# print('Записи (результат и имя):')
#
# for i_count in range(1, count + 1):
#     print(i_count, 'запись: ', end='')
#     record = tuple(input().split(' '))
#     score_dict[i_count] = record

print(score_dict)
# score_rates = [int(i_value[0]) for i_key, i_value in score_dict.items()]
# score_rates = sorted([int(i_value[0]) for i_key, i_value in score_dict.items()], reverse=True)[:3]
score_rates = sorted([int(i_value[0]) for i_key, i_value in score_dict.items()], reverse=True)
print(score_rates)

top_users = {}

for i_top, i_score in enumerate(score_rates):
    # print(i_top, i_score)
    for i_user in score_dict:
        if i_score == int(score_dict.get(i_user)[0]) and score_dict.get(i_user)[1] not in top_users.values():
            # print(score_dict.get(i_user)[0], score_dict.get(i_user)[1])
            # print(top_users.items())
            top_users[i_top] = score_dict.pop(i_user)
            break

print(top_users)
