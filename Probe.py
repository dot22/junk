sec = int(input('How many secs: '))

for i in range(sec - sec % 2, 0, -2):
    print(i)
