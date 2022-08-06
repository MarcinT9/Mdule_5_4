from faker import Faker
fake = Faker()
import random


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

sort_library_list = sorted(library_list, key=lambda movie: movie.title)

def get_movie():
    pass

def get_series():
    pass

def search(title):
    pass

def generate_views():
    random_movie = random.choice(library_list)
    random_number = random.randrange(1, 100)
    random_movie.number_of_plays = random_movie.number_of_plays + random_number
    print(f'{random_movie.title}, {random_movie.number_of_plays}')

def generate_views_times():
    for times in range(10):
        generate_views()

def top_title():
    pass

if __name__ == '__main__':
    movie = Movie(title='Nasz palneta', publishment=2019, grade='Document', number_of_plays=20)
    movie2 = Movie(title='BoJack Horseman', publishment=2014, grade='Drama', number_of_plays=10)
    movie3 = Movie(title='Stranger Tings', publishment=2016, grade='Sci-Fi', number_of_plays=15)
    series = Series(title='Dom z papieru', publishment=2017, grade='Thriller', number_of_plays=100, episode=2, season=3)
    series2 = Series(title='The Crown', publishment=2016, grade='Drama', number_of_plays=20, episode=7, season=1)
    series3 = Series(title='The Queen s Gambit', publishment=2020, grade='Action', number_of_plays=50, episode=3, season=5)

    movie.append_library_list()
    movie2.append_library_list()
    movie3.append_library_list()
    series.append_library_list()
    series2.append_library_list()
    series3.append_library_list()

    generate_views()
    generate_views_times()
