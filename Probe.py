class Family:
    surname = 'Common family'
    money = 100000
    have_a_house = False

    def info(self):
        print(
            'Family name: {}\nFamily funds: {}\nHaving a house: {}'.format(
                 self.surname, self.money, self.have_a_house
            )
        )

    def earn_money(self, amount):
