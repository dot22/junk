winners = 0
for number in 345, 19, 87, 1020, 421:
    if (99 < number < 1000) and number % 5 == 0:
        print('win number -', number)
        winners += 1
print('Winners -', winners)
