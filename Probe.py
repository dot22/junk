list_1 = [1, 2, 3, 4]
list_2 = 'word'

for i in range(4):
    print([value_1 for index_1, value_1 in enumerate(list_1)][i])
    print([value_2 for index_2, value_2 in enumerate(list_2)][i])

for index_1, value_1 in enumerate(list_1):
    print(index_1, value_1)

for index_2, value_2 in enumerate(list_2):
    print(index_2, value_2)

# list_f1 = [value_1 for index_1, value_1 in enumerate(list_1)]
# list_f2 = [value_2 for index_2, value_2 in enumerate(list_2)]
# print(list_f1)
# print(list_f2)
# list_f = [(value_1 for index_1, value_1 in enumerate(list_1)), (value_2 for index_2, value_2 in enumerate(list_2)) for i in range(4) if i == index_2]
# print(list_f)
