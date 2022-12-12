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

duration = 0.0
count = int(input('Сколько песен выбрать? '))
for i in range(count):
        query = 'Название ' + str(i + 1) + ' песни: '
        song = input(query)
        for cur_track in violator_songs:
            if cur_track[0] == song:
                duration += cur_track[1]

print(f'Общее время звучания песен: {round(duration, 2)} минут')