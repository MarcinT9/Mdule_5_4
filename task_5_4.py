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
        return f'{self.title} {self.publishment}'

    def __repr__(self):
        return f'Movie(title={self.title}, publishment={self.publishment}, grade={self.grade}, number_of_plays={self.number_of_plays})'


class Series(Movie):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f'{self.title} S{self.season:02d}E{self.episode:02d}'

    def __repr__(self):
        return f'Series(title={self.title}, publishment={self.publishment}, grade={self.grade}, number_of_plays={self.number_of_plays}, episode={self.episode:02d}, season={self.season:02d})'


def get_movies(library_list):
    list_movies= [i for i in library_list if type(i) == Movie]
    sort_list_movies = sorted(list_movies, key=lambda movie: movie.title) 
    return sort_list_movies

def get_series(library_list):
    list_series= [i for i in library_list if type(i) == Series]
    sort_list_series = sorted(list_series, key=lambda series: series.title)     
    return sort_list_series

def search(library_list, title):
    for i in library_list:
        if title == i.title:
            found_movie = i
    return found_movie
      
def generate_views(library_list):
    random_movie = random.choice(library_list)
    random_number = random.randrange(1, 100)
    random_movie.number_of_plays += random_number

def generate_views_times(library_list):
    for times in range(10):
        generate_views(library_list)

def top_titles(value):
    print(f'Najpopularniejsze filmy i seriale dnia {today_format}:')
    sort_by_number_of_plays = sorted(library_list, key=lambda movie: movie.number_of_plays, reverse=True)
    return sort_by_number_of_plays[:value]


if __name__ == '__main__':
    library_list = []
    today = date.today()
    today_format = today.strftime("%d.%m.%Y")

    movie = Movie(title='Nasza planeta', publishment=2019, grade='Document', number_of_plays=20)
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

    print('Biblioteka filmów')

    generate_views(library_list)
    print()

    print(top_titles(3))
    print()




