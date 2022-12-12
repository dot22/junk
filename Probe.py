def summa_n(number):
    summ = 0
    for i in range(1, number + 1):
        summ += i
    print('Summ is', summ)



digital = int(input('Enter the digital: '))
summa_n(digital)