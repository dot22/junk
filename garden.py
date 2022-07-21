class Potato:
    states = {0: 'None', 1: 'Early', 2: 'Green', 3: 'Good'}

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
        return False

    def print_state(self):
        print('Potato {} is in state {}'.format(self.index, Potato.states[self.state]))


class PotatoGarden:

    def __init__(self, count):
        self.potatos = [Potato(index) for index in range(0, count + 1)]

    def grow_all(self):
        for i_potato in self.potatos:
            i_potato.grow()

    def is_all_ripe(self):
        if not all(i_potato.is_ripe() for i_potato in self.potatos):
            print('Potato in not ripe yet\n')
        else:
            print('All potatos are ripe\n')
