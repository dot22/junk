def test():
    number = int(input('Enter the number: '))
    if number > 0:
        positive()
    if number < 0:
        negative()


def positive():
    print('Положительное')


def negative():
    print('Отрицательное')


test()
