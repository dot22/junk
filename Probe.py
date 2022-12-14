def first(tasks):
    result = 0
    for i in range(tasks):
        number = int(input('Enter the number: '))
        if number < 0:
            number = 0
        if number > result:
            result = number
    return result


number_of_tasks = int(input('How many tasks will be: '))
first_task = first(number_of_tasks)
print('The first task is', first_task)
