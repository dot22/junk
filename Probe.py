string = input('Enter the string: ')
position = 0
milk = 0

for i in string:
    position += 1
    if i == 'b':
        milk += position * 2

print(milk)