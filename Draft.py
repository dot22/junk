time = int(input('Enter the time: '))

if (time < 8) or (time >= 22) or (time == 14) or (10 <= time < 12) or (18 <= time < 20):
    print('Bad time')
else:
    print('Good time')
