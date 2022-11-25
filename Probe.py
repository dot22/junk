cost = int(input('Enter the cost: '))
size = int(input('Enter the size: '))

if (cost <= 10 and size >= 100) or (cost <= 7 and size >= 80):
    print('Good')
else:
    print('Bad')