import random
from datetime import date


class Movie:
    def __init__(self, title, publishment, grade, number_of_plays):
        self.title = title
        self.publishment = publishment
        self.grade = grade
        self.number_of_plays = number_of_plays 

    def play(self):
        self.number_of_plays += 1

    def __str__(self):
        return f'{self.title} {(self.publishment)}'

    def __repr__(self):
        return f'Movie(title={self.title}, publishment={self.publishment}, grade={self.grade}, number_of_plays={self.number_of_plays})'

    def append_library_list(self):
        library_list.append(self)


class Series(Movie):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f'{self.title} S{self.season:02d}E{self.episode:02d}'

    def __repr__(self):
        return f'Series(title={self.title}, publishment={self.publishment}, grade={self.grade}, number_of_plays={self.number_of_plays}, episode={self.episode:02d}, season={self.season:02d})'


library_list = []

def get_movies():
    list_movies= []
    for i in library_list:
        if not isinstance(i, Series):
            list_movies.append(i.title)
    sort_list_movies = sorted(list_movies)
    return sort_list_movies

def get_series():
    list_series= []
    for i in library_list:
        if isinstance(i, Series):
            list_series.append(i.title)
    sort_list_series = sorted(list_series)        
    return sort_list_series

def search():
    choice = input('Podaj tytuł: ')
    choice1 = choice.upper()
    for i in library_list:
        if choice1 == i.title.upper():
            if not isinstance(i, Series):
                print(f'{i.title} {i.publishment}')
            else:
                print(f"{i.title} S{i.season:02d}E{i.episode:02d}")

def generate_views():
    random_movie = random.choice(library_list)
    random_number = random.randrange(1, 100)
    random_movie.number_of_plays = random_movie.number_of_plays + random_number

def generate_views_times():
    for times in range(10):
        generate_views()

def top_titles(value):
    print(f'Najpopularniejsze filmy i seriale dnia {today_format}:')
    sort_by_number_of_plays = sorted(library_list, key=lambda movie: movie.number_of_plays, reverse=True)
    return sort_by_number_of_plays[:value]


if __name__ == '__main__':
    today = date.today()
    today_format = today.strftime("%d.%m.%Y")

    movie = Movie(title='Nasz palneta', publishment=2019, grade='Document', number_of_plays=20)
    movie2 = Movie(title='BoJack Horseman', publishment=2014, grade='Drama', number_of_plays=10)
    movie3 = Movie(title='Stranger Things', publishment=2016, grade='Sci-Fi', number_of_plays=15)
    series = Series(title='Dom z papieru', publishment=2017, grade='Thriller', number_of_plays=100, episode=2, season=3)
    series2 = Series(title='The Crown', publishment=2016, grade='Drama', number_of_plays=20, episode=7, season=1)
    series3 = Series(title='The Queen s Gambit', publishment=2020, grade='Action', number_of_plays=50, episode=3, season=5)

    library_list.append(movie)
    library_list.append(movie2)
    library_list.append(movie3)
    library_list.append(series)
    library_list.append(series2)
    library_list.append(series3)
    
    print('Biblioteka filmów:')
    print()

    for i in library_list:
        if not isinstance(i, Series):
            print(f'{i.title} {i.publishment}')
        else:
            print(f'{i.title} S{i.season:02d}E{i.episode:02d}')

    print()
    generate_views()
    print()

    print(top_titles(3))
    print()


    #search()
    #generate_views_times()
    #print(get_movies())
    #print(get_series())

