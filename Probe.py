class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

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


class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def info(self):





# potato_1 = Potato(1)
# potato_1.info()
# for _ in range(4):
#     potato_1.ruse()

my_garden = PotatoGarden(5)
print(PotatoGarden)