zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

zoo.insert(zoo.index('lion') + 1, 'bear')

zoo.remove('elephant')
print(zoo)
print(zoo.index('lion'))
print(zoo.index('monkey'))
