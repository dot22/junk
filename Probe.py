x = float(input('X: '))

while True:
    if x < 0 or x > 1:
        print('X wrong. Try another time:')
        x = float(input('X: '))
    else:
        break


y = float(input('Y: '))

while True:
    if y < 0 or y > 1:
        print('Y wrong. Try another time')
        y = float(input('Y: '))
    else:
        break

print('Your coordinates:', int(x * 10), int(y * 10))
