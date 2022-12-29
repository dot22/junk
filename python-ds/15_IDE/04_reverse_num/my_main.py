def reverse(number):
    reverse_part = ''
    first_part = ''
    for i in str(number):
        if i != '.':
            reverse_part = i + reverse_part
        else:
            first_part = reverse_part
            reverse_part = ''
    reverse_all = first_part + '.' + reverse_part
    return float(reverse_all)

    
first_number = 102.12
second_number = 123.34
reverse_first_number = reverse(first_number)
print('Первое число наоборот:', reverse_first_number)
reverse_second_number = reverse(second_number)
print('Второе число наоборот:', reverse_second_number)
print('Сумма:', reverse_first_number + reverse_second_number)
