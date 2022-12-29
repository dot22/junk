def nod(number):
    for i in range(2, number + 1):
        if number % i == 0:
            print('Наименьший делитель, отличный от единицы:', i)
            break
    return


first_number = 6
second_number = 17

nod(first_number)
nod(second_number)
