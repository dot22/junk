temperature = int(input('Введите температуру: '))
if temperature < 0 or temperature > 100:
    print('Alarm')
else:
    print('Good condition')
