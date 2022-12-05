numbers = int(input('Enter the number: '))
count = 0

for number in range(numbers):
    simple = False
    numeral = int(input('Enter numeral: '))
    for divisor in range(2, numeral):
        if numeral % divisor == 0:
            simple = True
    if simple == False:
        count += 1


print(count)
