class Movie:
    def __init__(self, name, genre, watched):
        self.name = name
        self.genre = genre
        self.watched = watched

    def __repr__(self):
        return "<Movie {}>".format(self.name)

    def jason(self):
        return {
            'name': self.name,
            'genre': self.genre,
            'watched': self.watched
        }
