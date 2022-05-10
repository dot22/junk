file_1 = open('/home/dot/Trash/task/group_1.txt', 'r')
summa = 0
for i_line in file_1:
    info = i_line.split()
    summa += int(info[2])

file_1 = open('/home/dot/Trash/task/group_1.txt', 'r')
diff = 0
for i_line in file_1:
    info = i_line.split()
    diff -= int(info[2])

file_2 = open('/home/dot/Trash/task/Additional_info/group_2.txt', 'r')
compose = 1
for i_line in file_2:
    info = i_line.split()
    compose *= int(info[2])

print(summa)
print(diff)
print(compose)
