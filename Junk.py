pacs_amount = int(input('Количество пакетов: '))
message = []
wrong_packs_amount = 0

for i in range(pacs_amount):
    print('Пакет номер', i + 1)
    packet = []
    for j in range(4):
        print(j + 1, 'пакет', end=' ')
        bit = int(input())
        packet.append(bit)
    if packet.count(-1) <= 1:
        message.extend(packet)
    else:
        wrong_packs_amount += 1
        print('Много ошибок в пакете')
    print()

print('Полученное сообщение:', message)
print('Количество ошибок в сообщении:', message.count(-1))
print('Количество потерянных пакетов:', wrong_packs_amount)
