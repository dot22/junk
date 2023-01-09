shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100],
        ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]

detail = 'седло'
amount = 0
cost = 0

for i_detail in shop:
        if i_detail[0] == detail:
                amount += 1
                cost += i_detail[1]

print('Название детали:', detail)
print('Количество деталей:', amount)
print('Общая стоимость:', cost)
