count = 0
while True:
    sequence = int(input('Enter next seq: '))
    if sequence == 0:
        break
    elif (sequence % 2) == 0:
        count += 1
print(count)
