class Potato:
    states: {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def print_state(self):
        print('Картошка {} в стадии {}'.format(
            self.index, self.state
        ))

    def grow(self):
        if self.state < 3:
            self.state += 1


class PotatoGarden:

    def __init__(self, count):
        self.potatos = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        for i_potato in self.potatos:
            i_potato.grow()
            print(i_potato.state)


my_garden = PotatoGarden(5)
my_garden.grow_all()
