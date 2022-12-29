data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "totalIn": 444,
        "totalOut": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "totalOut": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}

print('Задание 1. Вывести списки ключей и значений словаря.')
print('Список ключей словаря:', [x for x in data.keys()])
print('Список значений словаря:', [y for y in data.values()])
print()

print('Задание 2. В “ETH” добавить ключ “total_diff” со значением 100')
print(data['ETH'])
data['ETH']['total_diff'] = 100
print(data['ETH'])
print()

print('Задание 3. Внутри “fst_token_info” значение ключа “name” поменять с “fdf” на “doge”')
print(data['tokens'][0]['fst_token_info']['name'])
data['tokens'][0]['fst_token_info']['name'] = "doge"
print(data['tokens'][0]['fst_token_info']['name'])
print()

print('Задание 4. Удалить “total_out” из tokens и присвоить его значение в “total_out” внутри “ETH”.')
print(data["tokens"][1])
print(data["ETH"])
remove_datas_from_data = data['tokens'][1].popitem()
add_datas_to_ETH = {remove_datas_from_data[0]: remove_datas_from_data[1]}
data["ETH"].update(add_datas_to_ETH)
print(data["tokens"][1])
print(data["ETH"])
print()

print('5. Внутри "sec_token_info" изменить название ключа “price” на “total_price”.')
print(data['tokens'][1]['sec_token_info'])
data['tokens'][1]['sec_token_info']['total_price'] = data['tokens'][1]['sec_token_info'].pop('price')
print(data['tokens'][1]['sec_token_info'])

# зачёт!
