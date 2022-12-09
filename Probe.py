import math


h_angle = float(input('Angle of hour: '))

h_hour = h_angle // 30

print('Hour is:', int(h_hour))

m_angle = h_angle % 30 * 12


print(m_angle)