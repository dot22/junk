def resque(depth):
    result = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10
    return result


resque_level = 0.01
min_depth = 0
max_depth = 4
middle_depth = (min_depth + max_depth) / 2
while abs(resque(middle_depth)) - resque_level > 1e-15:
    if resque(middle_depth) < resque_level:
        max_depth = middle_depth
    else:
        min_depth = middle_depth
    middle_depth = (min_depth + max_depth) / 2
print(middle_depth)
