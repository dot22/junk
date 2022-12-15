def exp_string(digit):
    text = ''
    for i in digit:
        if i != 'e':
            text = text + i
        else:
            mantis = text
            text = ''
    print(mantis, 'dev', text)


number = (input('Enter the number: '))
exp_string(number)
