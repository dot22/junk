def extract_list(some_list, new_list=[]):
    for i_index in some_list:
        if isinstance(i_index, list):
            extract_list(i_index, new_list)
        else:
            new_list.append(i_index)
    return new_list


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

best_list = extract_list(nice_list)
print('Ответ:', best_list)
