def print_dict(some_dict):
    for i_piz in sorted(some_dict):
        print('\t', i_piz, ': ', some_dict[i_piz], sep='')


orders = int(input('Введите количество заказов: '))
cust_dict = {}

for i_order in range(1, orders + 1):
    print(i_order, 'заказ: ', end='')
    order = input('').split(' ')
    customer_name = order[0]
    pizza_name = order[1]
    pizza_amount = int(order[2])

    if customer_name in cust_dict:
        if pizza_name in cust_dict[customer_name].keys():
            cust_dict[customer_name][pizza_name] += pizza_amount
        else:
            cust_dict[customer_name][pizza_name] = pizza_amount
    else:
        cust_dict.setdefault(customer_name, {pizza_name: pizza_amount})

print()
for i_name in sorted(cust_dict):
    print(i_name, ':', sep='')
    print_dict(cust_dict[i_name])
