class Artist:
    def __init__(self, id, name, popularity, followers, genres):
        self.id = id
        self.name = name
        self.popularity = int(popularity)
        self.followers = int(followers)
        self.genres = genres

    def __str__(self):
        return self.id + '*' + self.name + '*' + str(self.popularity) + '*' + str(self.followers) + '*' + str(self.genres)