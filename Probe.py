def calc():
    number = int(input('Enter tne number: '))
    func = int(input('What to do? 1 - summ numeral, 2 - min numeral, 3 - max numeral: '))
    if func == 1:
        summ_numeral(number)
    elif func == 2:
        min_numeral(number)
        calc()
    elif func == 3:
        max_numeral(number)
        calc()
    else:
        print('Wrong choose')
        calc()


def summ_numeral(number):
    summ = 0
    while number > 0:
        summ += number % 10
        number //= 10
    print('Summ of numeral =', summ)
    calc()


def min_numeral(number):
    min_number = number % 10
    while number > 0:
        if number % 10 <= min_number:
            min_number = number % 10
        number //= 10
    print('Minimal digit =', min_number)


def max_numeral(number):
    max_number = number % 10
    while number > 0:
        if number % 10 >= max_number:
            max_number = number % 10
        number //= 10
    print('Max digit =', max_number)
    

calc()
