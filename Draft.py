orders = int(input('Введите количество заказов: '))
cust_dict = {}
common_dict = {}

for i_order in range(1, orders + 1):
    print(i_order, 'заказ: ', end='')
    order = input('').split(' ')
    order[2] = int(order[2])
    if order[0] in cust_dict.keys() and order[1] in cust_dict[order[0]].keys():
        order[2] += int(cust_dict[order[0]].get(order[1]))
    cust_dict[order[0]] = {order[1]: int(order[2])}
    print(cust_dict)
