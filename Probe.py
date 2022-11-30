wake_hour = int(input('Enter the hour: '))
total_cal = 0
water = 0

for i in range(wake_hour, 23, 3):
    print('Hour', i)
    water += 1
    cal = int(input('ENter the number of calories: '))
    total_cal += cal
print(water, total_cal)