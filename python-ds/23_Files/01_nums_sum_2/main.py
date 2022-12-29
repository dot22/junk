numbers_file = open('numbers.txt', 'r')
anser_file = open('answer.txt', 'w')
summ = 0

for i_number in numbers_file.read().split():
    summ += int(i_number)

anser_file.write(str(summ))

numbers_file.close()
anser_file.close()
