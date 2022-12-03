string = input('Enter the string: ')
position = 0

for letter in string:
    position += 1
    if letter == '*':
        break

print('Position number', position)
