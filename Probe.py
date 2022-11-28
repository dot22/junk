work_time = 8
count = 1
tasks = 0
wife_call = False
print('Начался 8-часовой рабочий день')

while count <= work_time:
    print(count, '-й час', sep='')
    count += 1
    jobs_assigned = int(input('How many jobs assigned: '))
    tasks += jobs_assigned
    wife_calling = int(input('Wife is calling. Answer the phone? 0/1 '))
    if wife_calling == 1:
        wife_call = True

print('Work time ended. Tasks done -', tasks)
if wife_call:
    print('Make shopping')
