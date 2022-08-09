class PotatoGarden:

    def __init__(self, amount):
        self.potatoes = [Potato(index) for index in range(1, amount + 1)]


class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0


class Gardener:

    def __init__(self, garden):
        # self.name = input('Введите имя садовника: ')
        self.garden = garden

    def harvest(self):
        print('До уборки урожая в грядке было {} шт. картошки'.format(len(self.garden.potatoes)))
        self.garden.potatoes = []
        print('После уборки урожая в грядке осталось {} шт. картошки'.format(len(self.garden.potatoes)))


my_garden = PotatoGarden(5)
new_gardener = Gardener(my_garden)
new_gardener.harvest()
