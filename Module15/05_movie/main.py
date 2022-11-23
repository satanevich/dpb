films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

favourites_films = []
films_number = int(input('Сколько фильмов хотите добавить? '))

for i in range(0, films_number):
    print('Введите название фильма: ', end='')
    movie = input()
    while movie not in films:
        print(f'Ошибка: фильма {movie} у нас нет :(')
        movie = input('Введите название фильма: ')
    else:
        favourites_films.append(movie)

print(f'\nВаш список любимых фильмов: {favourites_films}')
