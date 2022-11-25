range = int(input('Range of the student: '))

if range <= 10:
    grade = int(input('Grade of the student: '))
    print('Congratulation! You are a student now!')
    if grade >= 290:
        print('You will have a scholarship!')
    else:
        print("But you won't have a scholarship")
else:
    print('Unfortunately, you loose')
