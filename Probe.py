# bottom_c = int(input('Нижняя граница: '))
bottom_c = 0
# top_c = int(input('Верхняя граница: '))
top_c = 70
# step = int(input('Шаг: '))
step = 20

print('\nВывод')
print('C\tF')

for t_c in range(bottom_c, top_c, step):
    t_f = int(32 + t_c * 1.8)
    print(t_c, t_f, sep='\t')
    if t_c + step > top_c:
        t_f = int(32 + top_c * 1.8)
        print(top_c, t_f, sep='\t')

