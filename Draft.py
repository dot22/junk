while True:
    invitation = input('Введите шаблон адреса в формате {ip_address}: ')
    if '{ip_address}' in invitation:
        break
    else:
        print('Неправильный шаблон адреса. Повторите ввод.')


def insert_num():
    while True:
        i_num = int(input('Введите число: '))
        if 0 <= i_num <= 255:
            return i_num
        else:
            print('Неправильный ввод. Повторите еще раз')


ip_address = [str(insert_num()) for _ in range(4)]
ip_address = '.'.join(ip_address)
print(f'это адрес - {ip_address}')