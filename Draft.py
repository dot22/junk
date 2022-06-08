class Popato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        else:
            return False

    def print_state(self):
        print(
            'Картошка {} сейчас {}'.format(
                self.index, Popato.states[self.state]
            )
        )

class Garden:

    def __init__(self, count):
        self.popatoes = [Popato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает')
        for i_popato in self.popatoes:
            i_popato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.popatoes]):
            print('Картошка еще не созрела\n')
        else:
            print('Вся картошка созрела. Можно собирать')


my_garden = Garden(5)
my_garden.are_all_ripe()

for _ in range(3):
    my_garden.grow_all()
    my_garden.are_all_ripe()