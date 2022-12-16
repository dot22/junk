def count_range(start,stop):
    count = 0
    while start - stop > 1e-15:
        count += 1
        start -= start * 8.4 / 100
    print(count)


starting_point = float(input('Starting point: '))
stop_point = float(input('Stop point: '))

count_range(starting_point, stop_point)
