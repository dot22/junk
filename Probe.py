employes = int(input('Количество сотрудников: '))
salary_list = []

for i_emp in range(employes):
    print('Зарплата', i_emp + 1, 'сотрудника:', end=' ')
    salary = int(input(''))
    salary_list.append(salary)

print(salary_list)

for _ in salary_list:
    if 0 in salary_list:
        salary_list.remove(0)

print('Осталось сотрудников:', len(salary_list))
print('Зарплаты:', salary_list)
