# x_horse = float(input('Horse X: '))
# y_horse = float(input('Horse Y: '))
x_horse = 0.071
y_horse = 0.118

# x_new = float(input('New X: '))
# y_new = float(input('New Y :'))
x_new = 0.213
y_new = 0.068

x_hp = int(x_horse * 10)
y_hp = int(y_horse * 10)

x_nn = int(x_new * 10)
y_nn = int(y_new * 10)

if (abs(x_hp - x_nn) + abs(y_hp - y_nn) == 3) and (x_hp != x_nn and y_hp != y_nn):
    print('Good choise')
else:
    print('Wrong point')

print('Previous point: ', x_hp, y_hp)
print('Next point: ', x_nn, y_nn)


