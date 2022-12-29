number = int(input('Количество чисел: '))
chain_list = []

for _ in range(number):
    chain = int(input('Число: '))
    chain_list.append(chain)

count = 1

for i in range(1, len(chain_list)):
    if chain_list[::] == chain_list[::-1]:
        print('\nПоследовательность зеркальна')
        break
    elif chain_list[i:] != chain_list[-1: i - 1: -1]:
        count += 1
    else:
        print('\nПоследовательность: ', end='')
        print(*chain_list)
        print('Нужно приписать чисел:', count)
        print('Сами числа:', *chain_list[count - 1::-1])
        break

# зачёт!
