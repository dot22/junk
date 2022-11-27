bags = int(input('How many bags: '))
total_weight = 0
count_bags = 0
while count_bags < bags:
    count_bags += 1
    weight = int(input('Bags weight: '))
    total_weight += weight
    print('Перенесено', count_bags, 'из', bags)
print('Общий вес:', total_weight)
