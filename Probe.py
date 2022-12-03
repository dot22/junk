number = int(input('Enter the number: '))

for i in range(number // 10 + 1):
    print( '-=-' + str(i * 10), end='')
print('-=-')