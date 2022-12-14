def summ_n(dig):
    summ = 0
    for i in range(1, dig + 1):
        summ += i
    return summ


number = int(input('Enter the number: '))
new_number = summ_n(number)
print('summ from 1 til', number, '=', new_number)
another_number = summ_n(new_number)
print('summ from 1 til', new_number, '=', another_number)
