goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]

new_fruit = 'абрикосы'
price = 150

print('Текущий ассортимент:', goods)
print('\nНовый фрукт:', new_fruit)
print('Цена:', price)

goods.append([new_fruit, price])
print('\nНовый ассортимент:', goods)

for i_good in goods:
    i_good[1] += i_good[1] * 8 / 100
print('\nНовый ассортимент с увеличенной ценой:', goods)

