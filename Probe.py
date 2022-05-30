def divide(number):
    return 10 / number


def sum_of_divided(left, right):
    div_sum = 0
    for i_num in range(left, right + 1):
        try:
            div_sum += divide(i_num)
            print(div_sum)
        except ZeroDivisionError:
            print('На ноль делить нельзя')
    return div_sum


total = 2
try:
    numbers_file = open('numbers.txt', 'r')
    for i_line in numbers_file:
        nums_list = i_line.split()
        first_num = int(nums_list[0])
        second_num = int(nums_list[1])

        total += sum_of_divided(first_num, second_num)
    print('Общая сумма:', total)

except ZeroDivisionError:
    print('На ноль делить нельзя')

answer_file = open('answer.txt', 'w')
try:
    answer_file.write(int('The answer is: '))
    answer_file.write(total)
except TypeError:
    print('Ошибка записи в файл: тип данных не строка')
else:
    print('Программа выполнилась без ошибок')
finally:
    answer_file.close()
    print(answer_file.closed)
