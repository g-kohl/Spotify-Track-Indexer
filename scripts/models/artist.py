class Artist:
    def __init__(self, id, name, popularity, followers, genres, external_URLs):
        self.id = id
        self.name = name
        self.popularity = int(popularity)
        self.followers = int(followers)
        self.genres = genres
        self.external_URLs = external_URLs

    def __str__(self):
        return self.id + '*' + self.name + '*' + str(self.popularity) + '*' + str(self.followers) + '*' + str(self.genres) + '*' + str(self.external_URLs)