orders = int(input('Введите количество заказов: '))
cust_dict = {}

for i_order in range(1, orders + 1):
    print(i_order, 'заказ: ', end='')
    order = input('').split(' ')
    order[2] = int(order[2])
    cust_dict[order[0]][order[1]] = order[2]
    print(cust_dict)