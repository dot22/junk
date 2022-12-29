import random

team_1 = [round(random.uniform(5, 10), 2) for _ in range(20)]
team_2 = [round(random.uniform(5, 10), 2) for _ in range(20)]
print('Первая команда:', team_1)
print('Вторая команда:', team_2)
team_winners = [(team_1[i_order] if team_1[i_order] > team_2[i_order] else team_2[i_order]) for i_order in range(20)]
print('Победители тура:', team_winners)

# зачёт!
