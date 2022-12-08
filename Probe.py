import math

radius = float(input('Radius of the planet: '))
earth_volume = 10.8321e11

planet_volume = 4 / 3 * math.pi * radius ** 3

if planet_volume < earth_volume:
    print('Объём планеты Земля больше в', round(earth_volume / planet_volume, 3), 'раз')
else:
    inverse_coefficient = round(earth_volume / planet_volume, 3)
    coefficient = round(planet_volume / earth_volume, 3)
    print('Объём планеты Земля меньше в (1/', inverse_coefficient, ') = ', coefficient, 'раз', sep='')
