violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

time = 0
num = int(input('Сколько песен выбрать? '))

for i_num in range(1, num + 1):
    print('Название', i_num, 'песни: ', end='')
    song = input()
    for i_list in violator_songs:
        if i_list[0] == song:
            time += i_list[1]
            break

print('Общее время звучания песен:', round(time, 2), 'минут')

# зачёт!
