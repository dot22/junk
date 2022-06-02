import random


sym_sum = 0
line_count = 0

try:
    with open('people.txt', 'r') as peoples_file:
        for i_line in peoples_file:
            line_count += 1
            length = len(i_line)
            if i_line.endswith('\n'):
                length -= 1
            if length < 3:
                raise BaseException('Длина {} строки меньше трех символов'.format(line_count))
            sym_sum += length

except BaseException:
    print('Test')
finally:
    print(sym_sum)


def x_divide_y(x, y):
    try:
        x += random.randint(0, 10)
        y += random.randint(0, 5)
        return x / y
    except ZeroDivisionError:
        print('Ошибка в первой функции: на ноль делить нельзя')


def y_divide_x(x, y):
    try:
        x -= random.randint(0, 10)
        y -= random.randint(0, 5)
        return y / x
    except ZeroDivisionError:
        print('Ошибка во второй функции: на ноль делить нельзя')


try:
    with open('coordinates.txt', 'r') as file, open('result.txt', 'w') as file_2:
    # file = open('coordinates.txt', 'r')
    # file_2 = open('result.txt', 'w')
        for line in file:
            nums_list = line.split()
            res1 = x_divide_y(int(nums_list[0]), int(nums_list[1]))
            res2 = y_divide_x(int(nums_list[0]), int(nums_list[1]))
            number = random.randint(0, 100)
            my_list = sorted([res1, res2, number])
            print(' '.join(map(str, my_list)))
            file_2.write(' '.join(map(str, my_list)) + '\n')
except:
    print("Что-то пошло не так с первой функцией")
# finally:
#     file.close()
#     file_2.close()
