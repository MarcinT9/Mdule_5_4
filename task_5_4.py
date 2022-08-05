import random


class Movie:
    movie_list = []

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
        return f'Movie(title={self.title}, publishment={self.publishment}, grade={self.grade} number_of_plays={self.number_of_plays})'


class Series(Movie):
    series_list = []

    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season
        

    def __str__(self):
        return f'{self.title} S{self.season:02d}E{self.episode:02d}'

    def __repr__(self):
        return f'Series(title={self.title}, publishment={self.publishment}, grade={self.grade}, number_of_plays={self.number_of_plays}, episode={self.episode:02d}, season={self.season:02d})'


liberaty_list = [Movie.movie_list, Series.series_list]


def get_movie():
    pass

def get_series():
    pass

def search(title):
    pass

def generate_views():
    pass

def generate_viewa_times():
    for times in range(10):
        generate_views()

def top_title():
    pass

if __name__ == '__main__':
    pass



