number = float(input('Enter the number: '))
count = 0

while number > 10:
    count += 1
    number /= 10

print(number, count)