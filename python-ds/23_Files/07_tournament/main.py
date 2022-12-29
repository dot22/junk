read_file = open('first_tour.txt', 'r')
write_file = open('second_tour.txt', 'w')

first_tour_members = read_file.readline()
second_tour_members = 0

first_tour = read_file.readlines()
first_tour = [line.rstrip() for line in first_tour]

for i_member in first_tour:
    member_list = i_member.split(' ')
    if member_list[2] > first_tour_members:
        second_tour_members += 1

write_file.write(str(second_tour_members))
write_file.close()
write_file = open('second_tour.txt', 'a')

list_members = []
dict_members = {}
for i_member in first_tour:
    member_list = i_member.split(' ')
    if member_list[2] > first_tour_members:
        initial_name = member_list[1][0] + '.' + member_list[0]
        dict_members[initial_name] = member_list[2]

sorted_dict = {}
sorted_keys = sorted(dict_members, key=dict_members.get)

for i_member in range(1, len(sorted_keys) + 1):
    line = "\n" + str(i_member) + ') ' + sorted_keys[i_member - 1] + ' ' + dict_members[sorted_keys[i_member - 1]]
    write_file.write(line)
write_file.close()

print('Содержимое файла first_tour.txt:')
read_file = open('first_tour.txt', 'r')
print(read_file.read())
read_file.close()

print('Содержимое файла second_tour.txt:')
read_file = open('second_tour.txt', 'r')
print(read_file.read())
read_file.close()