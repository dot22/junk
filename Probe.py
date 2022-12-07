# x = float(input('X: '))
x = 0.731

while True:
    if x < 0 or x > 1:
        print('X wrong. Try another time:')
        x = float(input('X: '))
    else:
        break

# y = float(input('Y: '))
y = 0.167

while True:
    if y < 0 or y > 1:
        print('Y wrong. Try another time')
        y = float(input('Y: '))
    else:
        break

print('Your coordinates:', int(x * 10), int(y * 10))
# print(int(x * 10))
# print(x * 10)
#
# print(int(y * 10))
# print(y * 10)

if int(x * 10) + 0.5 > x * 10:
    x_center = round(((int(x * 10) + 0.5 - x * 10) / 10), 3)
else:
    x_center = (x * 10 - int(x * 10) + 0.5)

if int(y * 10) + 0.5 > y * 10:
    y_center = round(((int(y * 10) + 0.5 - y * 10) / 10), 3)
else:
    y_center = -round((y * 10 - int(y * 10) - 0.5) / 10, 3)
print(x_center)
print(y_center)
