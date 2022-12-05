n = int(input('Enter the N: '))

suma = 0
previous = 1       # Предыдущий факториал

for i in range(1, n + 1):
    current = previous * i    # Текущий факториал - см. примечание после кода
    suma += current
    previous = current

print(suma)