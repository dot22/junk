def print_dict(some_dict):
    print(some_dict)


orders = int(input('Введите количество заказов: '))
cust_dict = {}

for i_order in range(1, orders + 1):
    print(i_order, 'заказ: ', end='')
    order = input('').split(' ')
    order[2] = int(order[2])
    if order[0] in cust_dict.keys():
        cust_dict.get(order[0]).append({order[1]: order[2]})
    else:
        cust_dict.setdefault(order[0], [{order[1]: order[2]}])

for i_name in sorted(cust_dict):
    print(i_name)
    print_dict(cust_dict[i_name])
