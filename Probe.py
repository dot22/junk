from garden import PotatoGarden


my_garden = PotatoGarden(3)
my_garden.is_all_ripe()
for _ in range(3):
    my_garden.grow_all()
    my_garden.is_all_ripe()
