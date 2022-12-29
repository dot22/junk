employee_list = []

employee_numbers = 4

for _ in range(employee_numbers):
    idn = int(input('ID: '))
    employee_list.append(idn)

search_id = 20

if search_id in employee_list:
    print('Yes')
else:
    print('No')
