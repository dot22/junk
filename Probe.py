time = int(input('Enter the time: '))

if (8 <= time < 22) and ((time != 14) or (10 <= time < 12) or (18 <= time < 20)):
    print('Good time')
else:
    print('Bad time')
