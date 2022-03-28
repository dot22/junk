test_list = ['some', 'text']
test_dict = {'key': test_list}
for i in test_dict.values():
    print(*i)