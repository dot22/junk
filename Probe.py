goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# for i_goods in goods:
#     for i_store in store[goods.get(i_goods)]:
#         quantity = 0
#         summ = 0
#         # print(i_goods, i_store)
#         for i in i_store:
#             print(i_store[i])
#             print()
#         #     quantity += i['quantity']
#         #     summ += i['quantity'] * i['price']
#         # print('quantity', quantity)
#         # print('summ', summ)

for i_store in store:
    quantity = 0
    summ = 0
    for i in store.get(i_store):
        quantity += i['quantity']
        summ += i['price'] * i['quantity']
    print(i_store, quantity, summ)