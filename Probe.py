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

songs = 3
time = 0

for i_song in range(1, songs + 1):
    print('Название ', i_song, '-й песни: ', sep='', end='')
    song_title = input()
    for song in violator_songs:
        # print(song)
        if song[0] == song_title:
            time += song[1]

print('Общее время звучания песен:', round(time, 2))

