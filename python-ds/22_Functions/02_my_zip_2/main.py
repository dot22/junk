def gen_list(some_iter_1, some_iter_2):
    min_lenght = min(len(some_iter_1), len(some_iter_2))
    return ((some_iter_1[i_index], some_iter_2[i_index]) for i_index in range(min_lenght))


iter_1 = 'abcdef'
iter_2 = [1, 2, 3, 4]

final_list = list(gen_list(iter_1, iter_2))
print(final_list)
