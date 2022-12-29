def divide(number):
    divider = 2
    while number % divider != 0:
        divider += 1
    return divider


number = int(input('Введите число: '))
print('Наименьший делитель, отличный от единицы:', divide(number))

# зачёт!
