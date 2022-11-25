number = int(input('Enter the number: '))
summ = 0

while number > 0:
    if number % 10 == 5:
        break
    summ += number % 10
    number //= 10
print(summ)