min_sal = 0
flag = True

for i in range(10):
    cur_sal = int(input('Current salary: '))
    if cur_sal < min_sal:
        flag = False
    else:
        min_sal = cur_sal

if flag:
    print('Good salary')
else:
    print('Bad salary')
