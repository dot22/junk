nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

# cool_list = []
#
# for level_0 in nice_list:
#     for level_1 in level_0:
#         for level_2 in level_1:
#             cool_list.append(level_2)

cool_list = [level_2 for level_0 in nice_list for level_1 in level_0 for level_2 in level_1]

print(cool_list)

# зачёт!
