class PotatoGarden:

    def __init__(self, amount):
        self.potatoes = [Potato(index) for index in range(1, amount + 1)]

    def info(self):
        for i_potato in self.potatoes:
            print('Картошка {} в состоянии {}.'.format(i_potato.index, Potato.states[i_potato.state]))


class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0


class Gardener:

    def __init__(self, garden):
        self.name = input('Введите имя садовника: ')
        self.garden = garden

    def info(self):
        print('Садовник {} обслуживает грядку "{}".'.format(self.name, self.garden))

    def take_care_of_the_garden(self):
        print(self.garden)

    # def harvest(self):


my_garden = PotatoGarden(5)
# my_garden.info()
new_gardener = Gardener(my_garden)
# new_gardener.info()
new_gardener.take_care_of_the_garden()
print(len(my_garden.potatoes))
print(len(new_gardener.garden))
