class Movie:
    def __init__(self, title, publishment, grade, number_of_plays):
        self.title = title
        self.publishment = publishment
        self.grade = grade
        self.number_of_plays = number_of_plays


class Series(Movie):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season

