rows = int(input('Enter number of rows: '))
seats = int(input('Enter number of seats: '))
space = int(input('Free space in meters: '))

for i in range(rows):
    print('=' * seats + '*' * space + '=' * seats)
