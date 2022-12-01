sec = int(input('How many secs: '))

for i in range(sec, -1, -1):
    print('Now is', i, 'sec')
    ask = int(input('Do you want to stop? 0 or 1: '))
    if ask == 1:
        print('Timer was stopped at', i, 'sec')
        break

print('Warning! It is hot!')