numbers = 114, 12, 14, 10605, 4907, 450
for i in numbers:
    if i % 2 == 0 and i % 3 != 0:
        print(i, '- Good')
    else:
        print(i, ' - Bad')
