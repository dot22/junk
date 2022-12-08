# bottom_c = int(input('Нижняя граница: '))
bottom_c = 0
# top_c = int(input('Верхняя граница: '))
top_c = 50
# step = int(input('Шаг: '))
step = 20

print('\nВывод')
print('C\tF')

for t_c in range(bottom_c, top_c, step):
    t_f = int(32 + t_c * 1.8)
    print(t_c, t_f, sep='\t')
