import math


size = int(input('Enter file size: '))
speed = int(input('Enter connection speed: '))
count = 0
approximate_size = 0

while approximate_size < size:
    count += 1
    if approximate_size + speed < size:
        approximate_size += speed
    else:
        approximate_size = size
    percent_size = math.ceil(approximate_size / size * 100)
    print('Прошло ', count, ' сек. Скачано ', approximate_size, ' из ', size, ' Мб (', percent_size, '%)', sep='')

