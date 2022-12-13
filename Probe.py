import random


def rock_paper_scissors():
    machine = random.randint(1, 3)
    user = int(input('Камень - 1, Ножницы - 2, Бумага - 3: '))
    if (machine == 1 and user == 2) or (machine == 2 and user == 3) or (machine == 3 and user == 1):
        print('Machine =', machine, 'User =', user)
        print('Machine Win')
    elif (user == 1 and machine == 2) or (user == 2 and machine == 3) or (user == 3 and machine == 1):
        print('Machine =', machine, 'User =', user)
        print('User Win')
    else:
        print('Nobody win')
    print('\n')
    mainMenu()


def guess_the_number():
    number = random.randint(1, 100)
    print('Подсказка:', number)
    num_min = 1
    num_max = 100
    while True:
        guess = int(input('Guess the number: '))
        if number == guess:
            print('You are winner! Number is:', number)
            break
        else:
            print('Wrong number. Try again.')
            continue
    mainMenu()


def mainMenu():
    choice = int(input('Choice the game: 1 - scissors, 2 - numbers: '))
    if choice == 1:
        rock_paper_scissors()
    elif choice == 2:
        guess_the_number()
    else:
        print('Wrong number. Try another.')
        mainMenu()


mainMenu()
