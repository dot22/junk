def is_prime(number):
    if number > 1:
        for i_number in range(2, int(number / 2) + 1):
            if (number % i_number == 0):
                return False
        else:
            return True
    else:
        return False


def generate_crypt(some_text):
    return [i_data for i_index, i_data in enumerate(some_text) if is_prime(i_index)]


text = input('Введите итерируемый объект (кортеж, список, словарь, сроку): ')

## datas for tests
# text = 'О Дивный Новый мир!'
# text = [100, 200, 300, 'буква', 0, 2, 'а']
# text = [x for x in range(20)]

print(generate_crypt(text))
