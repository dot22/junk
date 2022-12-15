def num_reverse(num):
    reverse = ''
    for i in str(num):
        reverse = i + reverse

    return int(reverse)


num1 = int(input('Enter Number 1: '))
num2 = int(input('Enter Number 2: '))

num1_reverse = num_reverse(num1)
num2_reverse = num_reverse(num2)

sum_num = num1_reverse + num2_reverse
print(num_reverse(sum_num))

