start_num = int(input('Enter the start number: '))
finish_num = int(input('Enter the finish num: '))
div = int(input('Enter the divider: '))
summ = 0
count = 0

for i in range(start_num, finish_num + 1):
    if i % div == 0:
        count += 1
        summ += i

print('Result:', summ / count)
