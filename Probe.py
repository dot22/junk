import random
import string


def generate_random_tuple(length):
    letters = string.ascii_lowercase
    rand_tuple = tuple(random.choice(letters) for i in range(length))
    rand_letter = random.choice(letters)
    return rand_tuple, rand_letter


def generate_new_tuple(some_tuple, some_element):
    if some_tuple.count(some_element) == 0:
        new_tuple = ()
    elif some_tuple.count(some_element) == 1:
        some_element_index = some_tuple.index(some_element)
        new_tuple = some_tuple[some_element_index:]
    else:
        some_element_index = some_tuple.index(some_element)
        new_tuple = some_tuple[some_element_index:]
        # new_tuple = some_tuple[]
    return new_tuple


# random_tuple, random_letter = generate_random_tuple(15)

## some datas for tests
random_tuple = ('g', 'u', 'r', 'm', 's', 't', 'z', 'g', 'u', 'g', 'n', 'g', 'h', 'z', 'c')
random_letter = 'u'

print(random_tuple, random_letter)

print(generate_new_tuple(random_tuple, random_letter))