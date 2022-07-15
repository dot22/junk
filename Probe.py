class Potato:
    states = {0: 'Отсутствуе', 1: 'Росток', 2: 'Зеленая', 3: 'Созрела'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def info(self):
        print('Статус картошки {} - {}'.format(self.index, self.state))

    def ruse(self):
        if self.state < 3:
            self.state += 1
            print('Картошка {} сейчас {}'.format(self.index, Potato.states[self.state]))
        else:
            print('Вся картошка созрела. Можно собирать!')


# class PotatoGarden:


potato_1 = Potato(1)
potato_1.info()
potato_1.grow()
potato_1.info()

    def info(self):

    def info(self):
        print('Картошка {} сейчас {}'.format(self.index, self.state))

    def grow(self):
        if self.state < 3:
            self.state += 1
        print('Картошка {} на стадии {}'.format(self.index, states[self.state]))




# potato_1 = Potato(1)
# potato_1.info()
# for _ in range(4):
#     potato_1.ruse()

my_garden = PotatoGarden(5)
print(PotatoGarden)