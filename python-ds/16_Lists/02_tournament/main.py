team_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
team_first_day = []

for i in range(1, len(team_list), 2):
    team_first_day.append(team_list[i - 1])

print('Первый день:', team_first_day)

# зачёт!
