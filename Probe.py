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
score_rank = {int(i_value[0]): i_key  for i_key, i_value in score_dict.items()}
top_scores = sorted(score_rank)
top_score_1 = top_scores[-1]
top_score_2 = top_scores[-2]
top_score_3 = top_scores[-3]
# print(top_scores)
print(score_rank)
print(sorted(score_rank))
print(top_score_1)
print(top_score_2)
print(top_score_3)
