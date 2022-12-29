def find_err(incoming_list):
    for ip_part in incoming_list:
        if not ip_part.isdigit():
            print(ip_part, '- не целое число')
            return
        elif int(ip_part) > 255:
            print(ip_part, 'превышает 255')
            return
    print('IP-адрес корректен')


ip_list = input('Введите IP: ').split('.')

if len(ip_list) != 4:
    print('Адрес - это четыре числа, разделённые точками')
else:
    find_err(ip_list)

# зачёт!
