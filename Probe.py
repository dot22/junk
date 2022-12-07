import math


distance = float(input('Distance: '))
angle = float(input('Angle: '))
angle /= 57.2958

x = math.cos(angle) * distance
y = math.sin(angle) * distance

print(x, y)