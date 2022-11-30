count = 0

for i in range(10):
    number = int(input('Enter the number: '))
    if number > 0 and number % 2 == 0:
        print(number, '- Good')
        count += 1
print(count, 'goods')
