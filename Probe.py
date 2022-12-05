size = int(input('Enter the size of the piramid: '))

for i in range(size):
    print((size - i - 1) * ' ' + (i * 2 + 1) * '*')
