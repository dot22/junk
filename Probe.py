people = int(input('How many people: '))

for hour in range(people):
    print('Now hour is:', hour)
    for order in range(hour, people):
        print('Now order is: ', order)
    print()
print('Order finished!')
