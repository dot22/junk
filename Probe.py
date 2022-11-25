temperature = int(input('Temperature: '))
distance = 0

while temperature > 15:
    distance += 20
    temperature -= 2
    if temperature <= 15:
        break
    distance += 10
print('Distance =', distance)