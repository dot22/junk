# members = int(input('Общее количество участников: '))
# command = int(input('Количество человек в команде: '))

members = 12
command = 5
command_list = []
start = 1

if members % command == 0:
    for i in range(members // command):
        command_list.append(list(range(start, start + command)))
        start += command
    print('Общий список участников:', command_list)
else:
    print(members, 'участников невозможно поделить на команды по', command, 'человек')





