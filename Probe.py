week = 'понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье'
day = 0

question = input('Введите день недели: ')

for i in week:
    day += 1
    if question == i:
        print(day)
